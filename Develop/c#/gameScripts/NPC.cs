public class NPC {
    public static enum Type{
        Merchant,
        Aristocrat,
        Soldier,
        Warleader,
        Hunter,
        Traveler,
        Farmer,
        Citizen,
        Official,
        Assasin,
        Thief,
        Mage};

    public int pID;
    public int type;
    public int copperWealth;
    public int silverWealth;
    public int goldWealth;
    public int income;
    public int saturation;
    public int militaryStrength;
    public String name;
    public IBehaviourScript behaviour;


    public NPC(int type) {
        this.type = type;
    }

    void gen() {
        switch(type) {
            case NPC.Type.Merchant:
            break;
            case NPC.Type.Aristocrat:
            break;
            case NPC.Type.Soldier:
            break;
            case NPC.Type.Warleader:
            break;
            case NPC.Type.Hunter:
            break;
            case NPC.Type.Traveler:
            break;
            case NPC.Type.Farmer:
            break;
            case NPC.Type.Citizen:
            break;
            case NPC.Type.Official:
            break;
            case NPC.Type.Assasin:
            break;
            case NPC.Type.Thief:
            break;
            case NPC.Type.Mage:
            break;
        }
    }

}