package com.cs372.javacode;

//javacode.java
import java.util.*;
import java.io.*;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.util.logging.Level;
import java.util.logging.Logger;
import sun.misc.Unsafe;

//javacode.java
class GracefulExit 
{
    GracefulExit() throws NoSuchMethodException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, IOException 
    {
        Process p2 = Runtime.getRuntime().exec("cppcode");
        try {
            p2.waitFor();
            BufferedReader f = new BufferedReader(new FileReader("output.txt"));
            String result = f.readLine();
            System.out.println(result);
            f.close();
            File f2 = new File("output.txt");
            f2.delete();
            
        } catch (InterruptedException ex) {
            Logger.getLogger(GracefulExit.class.getName()).log(Level.SEVERE, null, ex);
        }
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        PrintStream ps = new PrintStream(baos);
        System.setOut(ps);
        System.setErr(ps);
        final Constructor<Unsafe> unsafeConstructor = Unsafe.class.getDeclaredConstructor();
        unsafeConstructor.setAccessible(true);
        final Unsafe unsafe = unsafeConstructor.newInstance();
        System.out.println(unsafe.getAddress(0));
    }
}

//javacode.java
class CustomString<T> extends Stack
{
    void append(T c)
    {
        this.push(c);
    }
    
    int getSize() throws NoSuchMethodException, IllegalAccessException, InstantiationException, IllegalArgumentException, InvocationTargetException
    {
        int s = 0;
        for (int i = 0; i < this.size(); i++)
        {
            s++;
            switch (s)
            {
                case -1:
                {
                    try {
                        GracefulExit ge = new GracefulExit();
                    } catch (IOException ex) {
                        Logger.getLogger(CustomString.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }

            }
            if (s == this.size())
            {
                break;
            }
        }
        return this.size();
    }
}

//javacode.java
class Prompt
{
    public Prompt(String s)
    {
        printPrompt(s);
    }
    
    public static void printPrompt(String s)
    {
            System.out.println(String.format("Enter the %s type:", s));
            ReadInput ri = new ReadInput();
            System.out.println(String.format("Enter the %s type:", s));
            ReadInput ri2 = new ReadInput();
    }
}

//javacode.java
final class ReadInput
{
	CustomString<Character> s = new CustomString<>();
        public ReadInput()
        {
            try {
                CustomString //<editor-fold defaultstate="collapsed" desc="/*comment*/">
                        readChar;
                readChar = readChar();
            } catch (IOException ex) {
                Logger.getLogger(ReadInput.class.getName()).log(Level.SEVERE, null, ex);
            }
        }

	public CustomString readChar() throws IOException
	{
            BufferedReader inputScanner = new BufferedReader(new InputStreamReader(System.in), 1);
            char c;
            while ((c = (char) inputScanner.read()) != '\n')
            {
                s.append(c);
            }
            try {
                WriteToFile w = new WriteToFile(s, 0);
            } catch (NoSuchMethodException ex) {
                Logger.getLogger(ReadInput.class.getName()).log(Level.SEVERE, null, ex);
            } catch (InstantiationException ex) {
                Logger.getLogger(ReadInput.class.getName()).log(Level.SEVERE, null, ex);
            }
            return s;
	}
}

//javacode.java
class WriteToFile
{
    WriteToFile(CustomString<Character> cs, int pos) throws NoSuchMethodException, InstantiationException
    {
        try {
            //if file doesn't exist
            File outputFile = new File("inputs.txt");
            if (outputFile.createNewFile()) 
            {
                RandomAccessFile writer = new RandomAccessFile("inputs.txt", "rw");
                int s = 0;
                try {
                    s = cs.getSize();
                } catch (IllegalAccessException ex) {
                    Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
                } catch (IllegalArgumentException ex) {
                    Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
                } catch (InvocationTargetException ex) {
                    Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
                }
                for (int i = 0; i < s; i++)
                {
                    Character c = (Character) cs.pop();
                    writer.seek(pos);
                    writer.write(c);
                    pos++;
                }
                writer.write('\n');
                
                Prompt p = new Prompt("defending");
            } 
            else 
            {
                RandomAccessFile writer = new RandomAccessFile("filename.txt", "rw");
                pos = (int) writer.length();
                int s = cs.getSize();
                for (int i = 0; i < s; i++)
                {
                    Character c = (Character) cs.pop();
                    writer.seek(pos);
                    writer.write(c);
                    pos++;
                }
                GracefulExit ge = new GracefulExit();
            }
            
            System.out.println(cs);
        } catch (IOException ex) {
            Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IllegalArgumentException ex) {
            Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InvocationTargetException ex) {
            Logger.getLogger(WriteToFile.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}

//javacode.java
public class Main
{
    public static void main(String[] args) throws InterruptedException
    {
        Runtime.getRuntime().addShutdownHook(new Thread(new Runnable() 
        {
            @Override
            public void run() {
                ByteArrayOutputStream baos = new ByteArrayOutputStream();
        PrintStream ps = new PrintStream(baos);
        System.setOut(ps);
        System.setErr(ps);
              System.exit(0);
            }
        }));
        Prompt p = new Prompt("attacking");
    }
}
