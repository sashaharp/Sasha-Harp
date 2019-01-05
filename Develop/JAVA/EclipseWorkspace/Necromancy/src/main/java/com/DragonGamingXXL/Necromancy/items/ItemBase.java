package com.DragonGamingXXL.Necromancy.items;

import com.DragonGamingXXL.Necromancy.Main;
import com.DragonGamingXXL.Necromancy.init.ModItems;
import com.DragonGamingXXL.Necromancy.util.IHasModel;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.item.Item;

public class ItemBase extends Item implements IHasModel
{

	public ItemBase(String name)
	{
		setUnlocalizedName(name);
		setRegistryName(name);
		setCreativeTab(CreativeTabs.MATERIALS);
		
		ModItems.ITEMS.add(this);
	}
	
	@Override
	public void registerModels() 
	{
		Main.proxy.registerItemRenderer(this, 0, "inventory");
	}

}
