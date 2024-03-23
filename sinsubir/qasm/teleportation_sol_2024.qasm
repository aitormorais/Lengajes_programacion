OPENQASM 2.0;
include "qelib1.inc";
gate message a {
  u3(pi / 8, pi / 3, 2.22) a;
}

qreg q[3];
creg cX[1];
creg cZ[1];

message q[0];

barrier q; // @phaseDisk
barrier q[0], q[1], q[2];
h q[1];
cx q[1], q[2];
cx q[0], q[1];
h q[0];
barrier q[0], q[1], q[2];

measure q[1] -> cX[0];
measure q[0] -> cZ[0];
if (cX == 1) x q[2];
if (cZ == 1) z q[2];