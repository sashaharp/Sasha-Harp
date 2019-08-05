/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gevocopy;

import java.io.File;
import javax.swing.JOptionPane;
import org.apache.commons.io.FileUtils;

/**
 *
 * @author sashaharp
 */
public class GeVoCopy {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        File srcDir = new File("O:\\040 Kundencenter\\055 Expert Banking Service\\4_Prozesse\\Böhm\\GVs\\Alle GVs");
        File finDir = new File("Q:\\001 Zusammenarbeit\\Kundencenter Data Room\\Geschäftsvorfälle-ab-2018-04-01\\GVs");
        try {
            FileUtils.copyDirectory(srcDir, finDir);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error: " + e.getMessage());
        }
    }
    
}
