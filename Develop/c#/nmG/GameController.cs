public class GameController {
    public static Player player;
    public static Target[] targets;
    public static Spell[] spells;

    public void Update() {
        player.Update();
        for(Target t : targets)
            t.Update();
        for(Spell s : spells) {
            if(s.Update())
                spells.remove(s);
        }
    }
}