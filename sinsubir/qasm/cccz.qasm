OPENQASM 2.0;
include "qelib1.inc";

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

qreg q[4];
x q[0];
x q[1];
x q[2];
h q[3];
cccz q[0], q[1], q[2], q[3];