package test;

import java.io.File;

import com.jacob.activeX.ActiveXComponent;
import com.jacob.com.ComThread;
import com.jacob.com.Dispatch;
import com.jacob.com.Variant;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Test {

    public static void main(String[] args) throws InterruptedException {
        File file = new File(".\\test.xlsm");
        String macroName = "TestM";

        SimpleDateFormat formatter = new SimpleDateFormat("HH");
        if(Integer.parseInt(formatter.format(new Date()))>12) {
            callExcelMacro(file, macroName);
        }
        while(true) {
            if(Integer.parseInt(formatter.format(new Date()))==12) {
                callExcelMacro(file, macroName);
            }
            if(args.length > 0)
                Thread.sleep(1000 * 60 * 5);
            else
                Thread.sleep(1000 * 60 * 59);
        }
    }

    private static void callExcelMacro(File file, String macroName) {
        ComThread.InitSTA(true);
        final ActiveXComponent excel = new ActiveXComponent("Excel.Application");
        try{
            excel.setProperty("EnableEvents", new Variant(false));

            Dispatch workbooks = excel.getProperty("Workbooks")
                    .toDispatch();

            Dispatch workBook = Dispatch.call(workbooks, "Open",
                    file.getAbsolutePath()).toDispatch();

            // Calls the macro
            Variant V1 = new Variant( file.getName() + macroName);
            Variant result = Dispatch.call(excel, "Run", new Variant("\'"+file.getName()+"\'!"+ macroName));

            // Saves and closes
            //Dispatch.call(workBook, "Save");

            //com.jacob.com.Variant f = new com.jacob.com.Variant(false);
            //Dispatch.call(workBook, "Close", f);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //excel.invoke("Quit", new Variant[0]);
            ComThread.Release();
        }
    }
}