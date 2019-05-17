public class Item {
    public static enum Category {
        defensive,
        offensive,
        household};
    public static enum Quality {
        small,
        medium,
        grand,
        epic};
    public int category;
    public int quality;
    public int avgCost;
    public bool military;
    public int num;
    public int discounts;
}