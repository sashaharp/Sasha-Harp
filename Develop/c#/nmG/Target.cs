public class Target {
    private int layer;

    public bool isTarget(int mask) {
        return (layer&mask) != 0;
    }

    public void Update() { }
}