male(james1).
male(charles1).
male(james2).
male(charles2).
male(george1).
male(paul).
female(catherine).
female(eliza).
female(sophia).
female(laura).
female(claudia).
parent(charles1,james1).
parent(eliza,james1).
parent(charles2,charles1).
parent(catherine,charles1).
parent(james2,charles1).
parent(sophia,eliza).
parent(george1,sophia).
parent(george1,paul).
parent(catherine,laura).
parent(charles2,laura).
parent(james2,laura).
parent(sopjia,paul).
parent(eliza,claudia).
parent(charles1,claudia).

father(Child,Dad):-male(Dad),parent(Child,Dad).

mother(Child,Mom):-female(Mom),parent(Child,Mom).

brother(Sib,Bro):-
    male(Bro),father(Sib,Father),father(Bro,Father),Bro\=Sib,mother(Sib,Mother),mother(Bro,Mother).


sister(Sib,Sis):-
    female(Sis),father(Sib,Father),father(Sis,Father),Sis\=Sib,mother(Sib,Mother),mother(Sis,Mother).

aunt(Kid,Auntie):- female(Auntie),parent(Kid,Parent),sister(Parent,Auntie).

aunt(Kid,Auntie):-
female(Auntie),parent(Kid,Person),brother(Person,Brother),married(Auntie,Brother).

uncle(Kid,UncleBuck):- male(UncleBuck),parent(Kid,Parent),brother(Parent,UncleBuck).

grandmother(Grandchild,Grandmother):-
female(Grandmother),parent(Grandchild,Parent),parent(Parent,Grandmother).

grandfather(Grandchild,Grandfather):-
male(Grandfather),parent(Grandchild,Parent),parent(Parent,Grandfather).
