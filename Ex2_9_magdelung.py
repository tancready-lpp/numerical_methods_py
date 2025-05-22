"""Exercise 2.9: The Madelung constant
In condensed matter physics the Madelung constant gives the total electric potential felt by an atom in a solid. It depends on the charges on the other atoms nearby and their locations.
Consider for instance solid sodium chloride—table salt. The sodium chloride crystal has atoms arranged on a cubic lattice, but with alternating sodium and chlorine atoms, the sodium ones having a single positive charge +e and the chlorine ones a single negative charge −e, where e is the charge on the electron. If we label each position on the lattice by three integer coordinates (i, j, k), then the sodium atoms fall at positions where i + j + k is even, and the chlorine atoms at positions where i + j + k is odd.
Consider a sodium atom at the origin, i = j = k = 0, and let us calculate the Madelung constant. If the spacing of atoms on the lattice is a, then the distance from the origin to the atom at position (i, j, k) is

sqrt((ia)^2 + (ja)^2 + (ka)^2)= a*sqrt(i^2 + j^2 + k^2),

and the potential at the origin created by such an atom is 

V(i, j, k) = ±e/(4π *eps0*  a*sqrt(i^2 + j^2 + k^2)) ,

with eps0 being the permittivity of the vacuum and the sign of the expression depending on whether i + j + k is even or odd. The total potential felt by the sodium atom is then the sum of this quantity over all other atoms. Let us assume a cubic box around the sodium at the origin, with L atoms in all directions. Then

V_tot = SUM(V(i, j, k)) {i,j,k=-L not i=j=k=0, to L} =  e/(4πeps0a) M,

where M is the Madelung constant, at least approximately—technically the Madelung constant is the value of M when L → ∞, but one can get a good approximation just by using a large value of L.
Write a program to calculate and print the Madelung constant for sodium chloride. Use as large a value of L as you can, while still having your program run in reasonable time—say in a minute or less.
"""
