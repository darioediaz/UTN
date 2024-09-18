package ar.edu.utnfc.backend;

public class Lista {
  private int [] v;
  private int size;

public Lista() {
  v = new int[100];
  size = 0;
}

  public void add(int x) {
    v[size] = x;
    size++;
  }
}
