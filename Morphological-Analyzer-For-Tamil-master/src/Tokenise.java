/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.*;
import java.util.logging.*;

/**
 *
 * @author Betina
 */
public class Tokenise {

    public static void tokenise(String file, int filenum) {
        BufferedReader br = null;
        BufferedWriter wr = null;

        int fileno = filenum;
        int count = 0;
        try {
//            String filename = "./Dataset/" + file.getName();
            int flag = 0;
            //fileno++;

//            Reader reader = new InputStreamReader(new FileInputStream(new File("./Dataset/file" + fileno + ".txt")), "UTF-8");
//            br = new BufferedReader(reader);
//            Writer writer = new OutputStreamWriter(new FileOutputStream(new File("./Token/input" + (fileno) + ".txt")), "UTF-8");
//            wr = new BufferedWriter(writer);
            Reader reader = new InputStreamReader(new FileInputStream(new File(file)), "UTF-8");
            br = new BufferedReader(reader);
            Writer writer = new OutputStreamWriter(new FileOutputStream(new File("./Token/input" + (fileno) + ".txt")), "UTF-8");
            wr = new BufferedWriter(writer);

            String line = null;
            String c = null;

            //boolean found=false;
            //wr.newLine();
            while ((line = br.readLine()) != null) {
                //wr.write(line);
                line = line.trim();
                if (line.length() > 0) {

                    String[] ctemp = line.split("\\s");
                    for (int i = 0; i < ctemp.length; i++) {
                        flag = 0;
                        count++;
                        ctemp[i]=ctemp[i].trim();
                        if (!ctemp[i].equals("")) {
                            if (ctemp[i].endsWith(".")) {
                                ctemp[i] = ctemp[i].replace(".", "");
                                flag = 1;
                            } else if (ctemp[i].startsWith(".")) {
                                ctemp[i] = ctemp[i].replace(".", "");
                            } else if ((ctemp[i].startsWith(",")) || (ctemp[i].endsWith(","))) {
                                ctemp[i] = ctemp[i].replace(",", "");
                            } else if ((ctemp[i].startsWith("*")) || (ctemp[i].endsWith("*"))) {
                                ctemp[i] = ctemp[i].replace("*", "");
                            } else if ((ctemp[i].startsWith("'")) || (ctemp[i].endsWith("*"))) {
                                ctemp[i] = ctemp[i].replace("'", "");
                            } else if ((ctemp[i].endsWith(":")) || (ctemp[i].startsWith(":"))) {
                                ctemp[i] = ctemp[i].replace(":", "");
                            } else if ((ctemp[i].startsWith("(")) || (ctemp[i].endsWith("("))) {
                                ctemp[i] = ctemp[i].replace("(", "");
                                ctemp[i] = ctemp[i].replace(")", "");
                            } else if ((ctemp[i].endsWith(")")) || (ctemp[i].startsWith(")"))) {
                                ctemp[i] = ctemp[i].replace(")", "");
                            } else if ((ctemp[i].endsWith("\"")) || (ctemp[i].startsWith("\""))) {
                                ctemp[i] = ctemp[i].replace("\"", "");
                            }
                            c = count + "";
                            if (!ctemp[i].equals("")) {
                                wr.write(ctemp[i]);

                                if (flag == 1) {
                                    wr.newLine();
                                    wr.write(".");
                                }
                                wr.newLine();
                            }
                            //freqOfTerms.put((String) ctemp[i], 0);
                        }
                    }
                }
            }
        } catch (Exception ex) {
            Logger.getLogger(Tokenise.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            try {
                br.close();
                wr.close();

            } catch (IOException ex) {
                Logger.getLogger(Tokenise.class.getName()).log(Level.SEVERE, null, ex);
            }
        }

        //stopwordRemoval();
        //analyse();
        //extractNoun();
        //countFrequencyOfTerms();
    }

    public static void main(String[] args) {

        try {

            String path = "./Dataset";
            //String files;
            File folder = new File(path);
            File[] listOfFiles = folder.listFiles();
            System.out.println("no of files!!!!!" + listOfFiles.length);
            int fileno = 0;

            for (int i = 0; i < listOfFiles.length; i++) {

                if (listOfFiles[i].isFile()) {
                    fileno++;
                    tokenise("./Dataset/"+listOfFiles[i].getName(), fileno);
                }
            }
        } catch (Exception ex) {
        }
    }
}
