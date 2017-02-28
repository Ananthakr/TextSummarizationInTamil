/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.*;
import org.apache.nutch.analysis.unl.ta.stemmer;
import org.apache.nutch.analysis.unl.ta.Analyser;
import py4j.GatewayServer;
/**
 *
 * @author ananth
 */
public class PythonInterface {
     //private StemDoc ste;
    /**
     * It is used to stem a sentence in module1
     * @param sent
     * @return 
     */
    public static String stemSent(String sent){
        String stemmedSent="";
        String[] words=sent.split("\\s+");
        for (String w : words){
          // System.out.print(w.trim()+"\n");
             String temp=stemmer.analyseF(w.trim(), true);
           // System.out.print(w.trim()+" : "+temp+"\n");
             stemmedSent+=temp+" ";
        }
       //System.out.print(stemmedSent);
       return stemmedSent;
    }
    
    
    public static String stemWord(String word){
        String stemmedWord="";
        String temp=stemmer.analyseF(word.trim(), true);
        if(temp!=null&&temp.isEmpty()){
            stemmedWord=temp;
        }
        return stemmedWord;
    }
    /**
     * It is used to analyze summarized sentence to extract information
     * @param sent
     * @return 
     */
    public static String analyseSent(String sent){
        String analysedSent="";
        String[] words=sent.split("\\s+");
        for (String w : words){
          // System.out.print(w.trim()+"\n");
             String temp=Analyser.analyseF(w.trim(), true);
           // System.out.print(w.trim()+" : "+temp+"\n");
             analysedSent+=temp+" ";
        }
        return analysedSent;
    }
    
     public static void main(String[] args){
        //String input=null;
        //String temp=null;
        
        GatewayServer gatewayServer = new GatewayServer(new PythonInterface());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        /*System.out.print("Enter sentence : ");
        try{
            input = br.readLine();
            //System.out.print(input);
        }catch(IOException e){
            e.printStackTrace();
        }
        
       System.out.print(stemSent(input));*/
    }
    
}
