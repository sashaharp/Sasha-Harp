public class Shop {
    public List<Item> items;
    public List<Area> areasOfInfluennce;
    public List<int> stockTypes;
    public bool militaryFlag;
    public bool assasinsFlag;
    public bool thiefsFlag;
    public bool royalFlag;
    public bool officialFlag;
    public int prestige;
    public int copperCapital;
    public int silverCapital;
    public int goldCapital;
    
    public Shop() {
        items = new List<Item>();
        areasOfInfluennce = new List<Area>();
        stockTypes = new List<int>();
    }
}