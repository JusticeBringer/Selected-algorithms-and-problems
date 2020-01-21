#include <iostream>
#include <vector>
#include <stack>

using namespace std;

const int MAX = 100000;

vector<int> adj[MAX];		//lista de adiacente
vector<int> adjInv[MAX];	//lista de adiacente inverse
bool visited[MAX];		 //vizitat pentru lista de adiacente
bool visitedInv[MAX];	//vizitat pentru lista de adiacente inverse
stack<int> s;

int scc[MAX];	//stim carei componente conexe un nod apartine
int counter = 1;	//numarul de componente conexe

// adaugam varfuri la graf
void addEdges(int a, int b){
	adj[a].push_back(b);
}

// adaugam varfuri la graful invers 
void addEdgesInverse(int a, int b){
	adjInv[b].push_back(a);
}

//functia va fi primul pas al algoritmului lui Kosaraju
void dfsFirst(int u){
	if (visited[u])
		return;

	visited[u] = 1;

	for (int i = 0; i < adj[u].size(); i++)
		dfsFirst(adj[u][i]);

	s.push(u);
}

//functia este al doilea pas al algoritmului lui Kosaraju
void dfsSecond(int u){
	if (visitedInv[u])
		return;

	visitedInv[u] = 1;

	for (int i = 0; i < adjInv[u].size(); i++)
		dfsSecond(adjInv[u][i]);

	scc[u] = counter;
}
 
//functie de ajutor pentru afisarea lui s
void showS(stack<int> s) {
	while (!s.empty()) {
		cout << s.top() << " ";
		s.pop();
	}
	cout << "\n\n";
}

//functie pentru construirea grafului normal si grafului invers
void makeGraph(int n, int m, int a[], int b[]) {
	for (int i = 0; i < m; i++){
		// x ramane x
		// -x va fi n - (-x) = n + x

		//Datorita formei normale Chomsky 
			// a[i] sau b[i] va fi -a[i] implica b[i]
            //                     -b[i] implica a[i]

		if (a[i] > 0 && b[i] > 0) {
			addEdges(a[i] + n, b[i]);
			addEdgesInverse(a[i] + n, b[i]);
			addEdges(b[i] + n, a[i]);
			addEdgesInverse(b[i] + n, a[i]);
		}

		else if (a[i] > 0 && b[i] < 0) {
			addEdges(a[i] + n, n - b[i]);
			addEdgesInverse(a[i] + n, n - b[i]);
			addEdges(-b[i], a[i]);
			addEdgesInverse(-b[i], a[i]);
		}

		else if (a[i] < 0 && b[i]>0) {
			addEdges(-a[i], b[i]);
			addEdgesInverse(-a[i], b[i]);
			addEdges(b[i] + n, n - a[i]);
			addEdgesInverse(b[i] + n, n - a[i]);
		}

		else {
			addEdges(-a[i], n - b[i]);
			addEdgesInverse(-a[i], n - b[i]);
			addEdges(-b[i], n - a[i]);
			addEdgesInverse(-b[i], n - a[i]);
		}
	}
}

//functie pentru verificarea 2-SAT
void is2Satisfiable(int n, int m, int a[], int b[]){
	
	//construim graful si graful invers
	makeGraph(n, m, a, b);

	//pas 1: traversam graful original
	for (int i = 1; i <= 2 * n; i++)
		if (!visited[i])
			dfsFirst(i);

	//pas 2: traversam graful invers si vom avea nr de componente conexe
	while (!s.empty()){

		showS(s);
		int n = s.top();
		s.pop();

		if (!visitedInv[n]){
			dfsSecond(n);
			counter++;
		}
	}

	for (int i = 1; i <= n; i++){
		if (scc[i] == scc[i + n]){ //daca avem x si -x in aceeasi componenta conexa expresia este nesatisfiabila
			cout << "Expresia este nesatisfiabila" << endl;
			return;
		}
	}

	//daca am ajuns aici inseamna ca nu am gasit x si -x in aceeasi componenta conexa, deci expresia este satisfiabila
	cout << "\t\t\tExpresia este satisfiabila\n\n"
		<< endl;
	return;
}

int main()
{
	int n = 5; //n este numarul de variabile
	int m = 7; //m este numarul de clauze

	// + va fi sau
	// * va fi si

	//Exemplul ales:
	// (x1+x2)*(x2’+x3)*(x1’+x2’)*(x3+x4)*(x3’+x5)* 
	// (x4’+x5’)*(x3’+x4) 
	int a[] = { 1, -2, -1, 3, -3, -4, -3 };
	int b[] = { 2, 3, -2, 4, 5, -5, 4 };

	is2Satisfiable(n, m, a, b);

	return 0;
}