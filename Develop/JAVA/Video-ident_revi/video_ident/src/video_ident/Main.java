package video_ident;

import java.io.BufferedReader;
import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.time.*;

public class Main {

	public static void main(String[] args) throws IOException {
		File[] dirs = new File("Q:\\001 Zusammenarbeit\\Video-Ident").listFiles(File::isDirectory);
		List<List<String[]>> table = new ArrayList<>();
		String temp = "";
		System.out.println("Video-Idents ab (TT.MM.JJJJ): ");
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		temp = in.readLine().replace(".", "-").trim();
		LocalDate fromDate = LocalDate.of(Integer.parseInt(temp.split("-")[2]), Integer.parseInt(temp.split("-")[1]), Integer.parseInt(temp.split("-")[0]));
		System.out.println("Video-Idents bis (TT.MM.JJJJ): ");
		temp = in.readLine().replace(".", "-").trim();
		LocalDate tillDate = LocalDate.of(Integer.parseInt(temp.split("-")[2]), Integer.parseInt(temp.split("-")[1]), Integer.parseInt(temp.split("-")[0]));
		for(File dir : dirs) {
			String y = dir.getName();
			if(y.charAt(0) == 'y' || y.charAt(0) == 'Y') {
				int n = table.size();
				table.add(new ArrayList<>());
				table.get(n).add(new String[] {y, "Datum:"});
				System.out.println("found Y: " + dir);
				File[] xmlfiles = dir.listFiles(new FilenameFilter() {
				    public boolean accept(File dir, String name) {
				        return name.toLowerCase().endsWith(".xml");
				    }
				});
				String[] s_xmlfiles = new String[xmlfiles.length];
				for(int n1 = 0; n1 < xmlfiles.length; n1++)
					s_xmlfiles[n1] = xmlfiles[n1].getAbsolutePath();
				Arrays.sort(s_xmlfiles);
				for(String xmlfile : s_xmlfiles) {
					String date = xmlfile.split("\\")[xmlfile.split("\\").length-1].substring(0,8);
					LocalDate Date = LocalDate.of(Integer.parseInt(date.substring(0,4)), Integer.parseInt(date.substring(4,2)), Integer.parseInt(date.substring(6,2)));
					if(fromDate.compareTo(Date) <= 0 && Date.compareTo(tillDate) <= 0) {
						try {
							
						} catch (Exception e) {
							
						}
					}
				}
			}
				
		}
	}

}
