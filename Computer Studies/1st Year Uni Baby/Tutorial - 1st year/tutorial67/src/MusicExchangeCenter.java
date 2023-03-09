import java.util.*;
public class MusicExchangeCenter {
    private  List<User> users;
    private Map<String,Float> royalties;
    private List<Song> downloadedSongs;

    public MusicExchangeCenter(){

        downloadedSongs = new ArrayList<Song>();
        users = new ArrayList<User>();
    }
    public void displayRoyalties(){
        /*float money = 0;
        List<String> artistName = new ArrayList<String>();
        for (Song s: allAvailableSongs()){
            for (Song g: allAvailableSongs()){
                if (s.getArtist().equals(g.getArtist())){
                    royalties.put(s.getArtist(),money+=0.25);
                }
            }
            System.out.println( "$"+String.format("%1.2f%20s",royalties.get(s.getArtist()),s.getArtist()));
            money = 0;
        }*/
    }
    public List<User> onlineUsers(){
        List<User> online = new ArrayList<User>();
        for (User u: users){
            if (u.isOnline()){
                online.add(u);
            }
        }
        return online;
    }

    public List<Song> allAvailableSongs(){
        List<Song> allSongs = new ArrayList<Song>();
        for (User u: users){
            if (u.isOnline()){
                for (Song s: u.getSongList()){
                    allSongs.add(s);
                }
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
        List<Song> artistSongs = new ArrayList<Song>();

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
                for (Song s : u.getSongList()) {
                    if (s.getTitle().equals(title)) {
                        downloadedSongs.add(s);

                        return s;
                    }
                }
            }

        }
        return null;
    }

    public TreeSet<Song> uniqueDownloads(){
        TreeSet<Song> listOfSortSongs = new TreeSet<Song>();
        for (Song s: allAvailableSongs()){
            listOfSortSongs.add(s);
        }
        return listOfSortSongs;
    }

    public ArrayList<Pair> songsByPopularity(){
        ArrayList<Pair> pair = new ArrayList<Pair>();

        int counter = 0;
        for (Song s: downloadedSongs){
            for (Song g: downloadedSongs){
                if (s.getTitle().equals(g)){
                    counter++;

                }
            }
            pair.add(new Pair(counter,s));
        }
        return pair;
    }

    public int compare(Pair<Integer, Song> p1, Pair<Integer, Song> p2) {
        return p1.getKey()-p2.getKey();
    }

}
