public class Spell {
    public int energy = 2;
    public double duration = 5;
    public Vector2 location;
    public double radius;

    public bool Update() {
        duration -= Time.deltaTime;
        if(duration < 0) {
            return true;
        }
        return false;
    }
}