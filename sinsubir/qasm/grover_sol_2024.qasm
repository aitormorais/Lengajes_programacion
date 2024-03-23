OPENQASM 2.0;
include "qelib1.inc";

gate oracle a, b, c, d {
  x b;
  cu3(0, pi / 4, 0) a, d;
  cx a, b;
  cu3(0, -pi / 4, 0) b, d;
  cx a, b;
  cu3(0, pi / 4, 0) b, d;
  cx b, c;
  cu3(0, -pi / 4, 0) c, d;
  cx a, c;
  cu3(0, pi / 4, 0) c, d;
  cx b, c;
  cu3(0, -pi / 4, 0) c, d;
  cx a, c;
  cu3(0, pi / 4, 0) c, d;
  x b;
}

gate cccz a, b, c, d {
  cu1(pi / 4) a, d;

  cx a, b;

  cu1(-pi / 4) b, d;

  cx a, b;

  cu1(pi / 4) b, d;

  cx b, c;

  cu1(-pi / 4) c, d;

  cx a, c;

  cu1(pi / 4) c, d;

  cx b, c;

  cu1(-pi / 4) c, d;

  cx a, c;

  cu1(pi / 4) c, d;
}
gate ism a, b, c, d {
  h a;
  h b;
  h c;
  h d;
  x a;
  x b;
  x c;
  x d;
  cccz a, b, c, d;
  x a;
  x b;
  x c;
  x d;
  h a;
  h b;
  h c;
  h d;
}

gate iterator a, b, c, d {
  oracle a, b, c, d;
  ism a, b, c, d;
}

qreg q[4];

h q[0];
h q[1];
h q[2];
h q[3];

iterator q[0], q[1], q[2], q[3];

iterator q[0], q[1], q[2], q[3];

iterator q[0], q[1], q[2], q[3];