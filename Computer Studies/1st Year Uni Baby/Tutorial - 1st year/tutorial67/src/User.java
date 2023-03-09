import java.util.ArrayList;
import java.util.List;

public class User {
  private String     userName;
  private boolean    online;
  private List<Song> songList;
  
  public User()  { this(""); }
  
  public User(String u)  {
    userName = u;
    online = false;
    songList = new ArrayList<>();
  }

  public List<Song> getSongList(){return songList;}
  public String getUserName() { return userName; }
  public boolean isOnline() { return online; }

  public void addSong (Song s){
    if (!(this == null)) {
      songList.add(s);
    }
  }

  public List<String> requestCompleteSonglist(MusicExchangeCenter m){
    List<String> list = new ArrayList<String>();
    list.add(String.format("%-33s%-15s%10s%15s","TITLE","ARTIST","TIME","OWNER") + "\n");
    int counter = 1;
    for (User u: m.onlineUsers()){
      for (Song s: u.songList){
        list.add(String.format("%-3s%-30s%-21s%-2s%-12s%-15s",counter+".",s.getTitle(),s.getArtist(),s.getMinutes()+":",s.getSeconds(),u.getUserName()));
        counter++;
      }
    }
    return list;
  }

  public List<String> requestSonglistByArtist(MusicExchangeCenter m, String artist){
    List<String> list = new ArrayList<String>();
    list.add(String.format("%-33s%-15s%10s%15s","TITLE","ARTIST","TIME","OWNER") + "\n");
    int counter = 1;
    for (User u: m.onlineUsers()){
      for (Song s: u.songList){
        if(s.getArtist().equalsIgnoreCase(artist)){
          list.add(String.format("%-3s%-30s%-21s%-2s%-12s%-15s",counter+".",s.getTitle(),s.getArtist(),s.getMinutes()+":",s.getSeconds(),u.getUserName()));
          counter++;
        }
      }
    }
    return list;
  }

  public boolean songWithTitle(String title){
    for (Song s: songList){
      if(s.getTitle().equals(title)){
        return true;
      }
    }
    return false;
  }

  public void downloadSong(MusicExchangeCenter m, String title, String ownerName){
    if(!(null == m.getSong(title, ownerName))){
      System.out.println("NULL");
      songList.add(m.getSong(title,ownerName));

    }


  }
  public int totalSongTime(){
    int sum = 0;
    for(Song s: songList){
      sum += s.getDuration();
    }
    return sum;
  }

  public void register(MusicExchangeCenter m){
    m.registerUser(this);
  }

  public void logon(){
    online = true;
  }

  public void logoff(){online =false;}

  public String toString()  {
    String s = "" + userName + ": "+ songList.size() + " songs (";
    if (!online) s += "not ";
    return s + "online)";
  }
}
