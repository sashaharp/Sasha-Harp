package com.sashaharp.zerti;

public class Zerti {

	public static void main(String[] args) {
		IGUI g;
		IZertiController c;
		if(args.length > 0) {
			g = new AdminGUI();
			c = new AdminController();
		} else {
			g = new UserGUI();
			c = new UserController();
		}
		c.init(g);
	}

}
