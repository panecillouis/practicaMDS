import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;



public class VisitCounter_Solved {
    private static final String FILE_NAME = "visit_count.txt";
    // Usamos un objeto para sincronizar el acceso al archivo para que solo un hilo pueda acceder al archivo a la vez
    private static final Object fileSync = new Object();
    private static final Logger LOGGER = Logger.getLogger(VisitCounter_Solved.class.getName());


    // No usamos la old_counter asi que no lo incluimos en este codigo y usaremos  unicamente incrementVisitCount
    public static void incrementVisitCount() {
        // Para evitar que varios hilos incrementen el contador al mismo tiempo, usamos una sincronización bloqueada
        synchronized (fileSync) {
            //Usamos RandomAccessFile a la hora de leer y escribir en el archivo para evitar problemas de concurrencia
            //Y de ahi que usemos el Lock, nos sirve para la sincronizacion de hilos
            try (RandomAccessFile archivo = new RandomAccessFile(FILE_NAME, "rw");
                 FileChannel canal = archivo.getChannel();
                 FileLock lock = canal.lock()) {
                // Leemos el contador de visitas del archivo, como String y lo convertimos a entero
                String linea = archivo.readLine();
                int currentCount;
                if (linea == null || linea.trim().isEmpty()) {
                    currentCount = 0;
                } else {
                    try {
                        currentCount = Integer.parseInt(linea);
                    } catch (NumberFormatException e) {
                        LOGGER.log(Level.WARNING, "Formato numérico inválido en el archivo, se reinicia el contador.", e);
                        currentCount = 0;
                    }
                }
                currentCount++;
                archivo.seek(0);
                archivo.setLength(0);
                archivo.writeBytes(String.valueOf(currentCount));

            } catch (IOException e) {
                LOGGER.log(Level.WARNING, "Error al incrementar el contador de visitas.", e);
            }
        }
    }

    public static void main(String[] args) {

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME))) {
            writer.write("0");
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Error inicializando el archivo del contador de visitas.", e);
            return;
        }

        ExecutorService executor = Executors.newFixedThreadPool(10);
        for (int i = 0; i < 1000; i++) {
            executor.submit(VisitCounter_Solved::incrementVisitCount);
        }

        executor.shutdown();
        try {
            if (!executor.awaitTermination(1, TimeUnit.MINUTES)) {
                LOGGER.warning("No se completaron todas las tareas en el tiempo previsto.");
            }
        }
        catch(InterruptedException e){
                LOGGER.log(Level.SEVERE, "Hilo interrumpido mientras se esperaba la finalización.", e);
                executor.shutdownNow();
        }
    }

}

   