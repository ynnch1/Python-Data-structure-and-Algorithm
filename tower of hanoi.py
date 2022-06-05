def TowerOfHanoi(n , a_pole, c_pole, b_pole):           
    if n == 1:
        print("Move disc 1 from pole",a_pole,"to pole",c_pole)
        return
    TowerOfHanoi(n-1, a_pole, b_pole, c_pole)
    print("Move disc",n,"from pole",a_pole,"to pole",c_pole)
    TowerOfHanoi(n-1, b_pole, c_pole, a_pole)
 
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')