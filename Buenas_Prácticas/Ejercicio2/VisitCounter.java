//En este documento identificamos las vulnerabilidades y las corregiremos en otro documento
// La principal vulnerabilidad que se esta produciendo es la condicion de carrera que se produce porque varios hilos estan accediendo a la variable count sin sincronizacion
// Tambien se produce una vulnerabilidad de lectura y escritura de archivos sin control de errores 
// Las correcciones las veremos a partir de incrementVisitCount ya que oldCounter no se usa

package es.urjc.etsii.grafo.CPIF;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class VisitCounter {
    private static final String FILE_NAME = "visit_count.txt";
    private static int count = 10;

    // CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')

    public static void old_counter() throws IOException {
        count+=1;
        BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME)); //Bug here
        writer.write(String.valueOf(count));
        writer.close();
    };
    // Simulate visit by incrementing the count
    // CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
    
    public static void incrementVisitCount() {
        try {
            // Read the current count from the file
            // CWE-404: Improper Resource Shutdown or Release
            BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME));
            //CWE-20: Improper Input Validation
            int currentCount = Integer.parseInt(reader.readLine());
            reader.close();

            // Increment the count
            // CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition

            currentCount++;

            // Write the updated count back to the file
            // CWE-404: Improper Resource Shutdown or Release
            BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME));
            writer.write(String.valueOf(currentCount));
            writer.close();
        } catch (IOException e) {
            e.printStackTrace(); //CWE-209: Generation of Error Message Containing Sensitive Information

        }
    }
    // CWE-703: Improper Check or Handling of Exceptional Conditions
    public static void main(String[] args) throws InterruptedException, IOException {
        // Set the initial visit count to 0
        // CWE-772: Missing Release of Resource after Effective Lifetime
        BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME));
        writer.write("0");
        writer.close();

        ExecutorService executor = Executors.newFixedThreadPool(10);
        for (int i = 0; i < 1000; i++) {
            executor.submit(VisitCounter::incrementVisitCount);
        }

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);
    }
}

