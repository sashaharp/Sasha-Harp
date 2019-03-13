using System;
using System.Windows.Forms;
using Gtk;

public partial class MainWindow : Gtk.Window
{
    public MainWindow() : base(Gtk.WindowType.Toplevel)
    {
        Build();
    }

    protected void OnDeleteEvent(object sender, DeleteEventArgs a)
    {
        Gtk.Application.Quit();
        a.RetVal = true;
    }

    protected void OnButton1Clicked(object sender, EventArgs e)
    {
        MessageBox.Show(entry1.Text);
    }

}
