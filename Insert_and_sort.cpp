#include <iostream>

using namespace std;

struct node
{
	int info;
	node* next;

}*first, *last;

typedef node* nod;

void afisareLista()
{
	node* p = first;
	while (p != NULL)
	{
		cout << p->info << " ";
		p = p->next;

	}
}
void adf(int x)
{
	if (last == NULL)
	{
		first = last = new node;
		last->info = x;
		last->next = NULL;
	}
	else
	{
		node* temporar = new node;
		temporar->info = x;
		temporar->next = NULL;
		last->next = temporar;
		last = temporar;

	}
}

void inserareSortare (int x)
{
	node *p = first;
	node *beforeP = NULL;
	if (first == NULL)
	{
		adf(x);
		return;
	}

	while (p != NULL && (p->info) < x)
	{

		beforeP = p;
		p = p->next;

	}

	node *temporar = new node;
	temporar->info = x;
	
	if (beforeP == NULL)
	{
		temporar->next = p;
		first = temporar;

		return;
	}
	
	beforeP->next = temporar;
	temporar->next = p;
}

int main()
{
	int n = 0, i = 0, x=0;


	cout << "n=";
	cin >> n;

	for (i = 0; i < n; i++)
	{
		cout << "x=";
		cin >> x;
		cout << endl;
		inserareSortare(x);
	}

	afisareLista();
	return 0;
}