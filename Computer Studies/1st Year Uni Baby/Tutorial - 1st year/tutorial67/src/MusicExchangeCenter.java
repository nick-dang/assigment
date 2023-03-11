import java.util.*;
public class MusicExchangeCenter  {
    private  List<User> users;
    private Map<String,Float> royalties;
    private List<Song> downloadedSongs;

    public MusicExchangeCenter(){
        royalties = new HashMap<>();
        downloadedSongs = new ArrayList<>();
        users = new ArrayList<>();
    }
    public void displayRoyalties(){
        for(Pair<Integer,Song> pair: songsByPopularity() ){
            float money = pair.getKey()*0.25f;
            String artistName = pair.getValue().getArtist();
            royalties.put(artistName, royalties.get(artistName)+money);
        }
        System.out.println("Amount   Artist\n----------------");
        for (Map.Entry<String,Float> entry: royalties.entrySet()){
            System.out.println("$"+String.format("%-8.2f%-10s",entry.getValue(),entry.getKey()));
        }
    }

    public List<User> onlineUsers(){
        List<User> online = new ArrayList<>();
        for (User u: users){
            if (u.isOnline()){
                online.add(u);
            }
        }
        return online;
    }

    public List<Song> allAvailableSongs(){
        List<Song> allSongs = new ArrayList<>();
        for (User u: users){
            if (u.isOnline()){
                allSongs.addAll(u.getSongList());
            }
        }
        return allSongs;
    }

    public String toString(){
        return "Music Exchange Center (" + onlineUsers().size() + " users online, " + allAvailableSongs().size()+
                " songs available)";
    }
    public List<Song> getDownloadedSongs(){return downloadedSongs;}
    public User userWithName (String s){
        for (User u: users){
            if (u.getUserName().equalsIgnoreCase(s)){
                return u;
            }
        }
        return null;
    }

    public void registerUser (User x){
        String name = x.getUserName();
        if(userWithName(name) == null){
            users.add(x);
        }
    }

    public List<Song> availableSongsByArtist (String artist){
        List<Song> artistSongs = new ArrayList<>();

        for (Song s: allAvailableSongs()){
            if(s.getArtist().equalsIgnoreCase(artist)){
                artistSongs.add(s);
            }
        }
        return artistSongs;
    }

    public Song getSong(String title, String ownerName) {
        for (User u : onlineUsers()) {
            if (u.getUserName().equals(ownerName)) {
                Song s = u.songWithTitle(title);
                if (s != null) {
                    downloadedSongs.add(s);
                    royalties.put(s.getArtist(),0f);
                    return s;
                }
            }
        }
        return null;
    }

    public TreeSet<Song> uniqueDownloads(){
        return new TreeSet<>(downloadedSongs);
    }

    public ArrayList<Pair<Integer,Song>> songsByPopularity(){
        ArrayList<Pair<Integer,Song>> listOfPair = new ArrayList<>();
        for (Song s: uniqueDownloads()){
            listOfPair.add(new Pair<>(0,s));
        }
        for (Song s: downloadedSongs){
            for (Pair<Integer, Song> pair : listOfPair) {
                if (s.equals(pair.getValue())) {
                    pair.setKey(pair.getKey() + 1);
                    break;
                }
            }
        }
        listOfPair.sort((p1, p2) -> p2.getKey() - p1.getKey());
        return listOfPair;
    }


}
