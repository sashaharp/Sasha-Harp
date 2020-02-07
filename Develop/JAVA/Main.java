package com.sashaharp.JPixel;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

import javax.imageio.ImageIO;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedImage i = null;
		Errors res = loadImage("C:\\Users\\Admin\\Documents\\test.png", i);
		if (res == Errors.NONE) {
			System.out.println("Success!");
		} else {
			System.out.println(res.toString());
		}
	}

	
	public static Errors loadImage(String path, BufferedImage i) throws IOException {
		File imFile = new File(path);
		if(!imFile.exists()) 
			return Errors.FILE_NOT_FOUND;
		if(path.length() < 4 || !path.substring(path.length()-4).equalsIgnoreCase(".png") || !Files.probeContentType(imFile.toPath()).equalsIgnoreCase("image/png")) 
			return Errors.FORMAT_ERROR;
		i = ImageIO.read(imFile);
		return Errors.NONE;
	}
}

enum Errors {
	NONE, FORMAT_ERROR, FILE_NOT_FOUND,
};