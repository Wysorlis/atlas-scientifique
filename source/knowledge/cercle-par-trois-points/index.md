# Cercle passant par trois points

<div class="note-meta">
<p><strong>Domaines :</strong> mathématiques, géométrie analytique, algèbre linéaire</p>
<p><strong>Synonymes :</strong> cercle par trois points, cercle circonscrit, circumcircle, ajustement exact d'un cercle</p>
<p><strong>Mots-clés :</strong> points non alignés, équation cartésienne, système linéaire, déterminant, centre, rayon</p>
</div>

Trois points non alignés déterminent un unique cercle. Les notes construisent
ce cercle de deux manières équivalentes : en résolvant un système linéaire pour
les coefficients de son équation, puis en écrivant directement une équation
par déterminant.

## Équation générale du cercle

On part de l'équation cartésienne normalisée

$$
x^2+y^2+ax+by+c=0,
$$

où $a$, $b$ et $c$ sont inconnus.

Soient trois points

$$
A=(x_A,y_A),\qquad
B=(x_B,y_B),\qquad
C=(x_C,y_C).
$$

Pour que chacun appartienne au cercle, ses coordonnées doivent vérifier
l'équation précédente. On obtient donc les trois lignes manuscrites :

$$
\left\{
\begin{aligned}
x_A^2+y_A^2+a x_A+b y_A+c&=0, \\
x_B^2+y_B^2+a x_B+b y_B+c&=0, \\
x_C^2+y_C^2+a x_C+b y_C+c&=0.
\end{aligned}
\right.
$$

En isolant les termes connus, ce système devient

$$
\left\{
\begin{aligned}
a x_A+b y_A+c&=-(x_A^2+y_A^2), \\
a x_B+b y_B+c&=-(x_B^2+y_B^2), \\
a x_C+b y_C+c&=-(x_C^2+y_C^2).
\end{aligned}
\right.
$$

Il s'écrit sous forme matricielle

$$
\begin{pmatrix}
x_A & y_A & 1 \\
x_B & y_B & 1 \\
x_C & y_C & 1
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c
\end{pmatrix}
=
-\begin{pmatrix}
x_A^2+y_A^2 \\
x_B^2+y_B^2 \\
x_C^2+y_C^2
\end{pmatrix}.
$$

Le système admet une solution unique lorsque

$$
\det\begin{pmatrix}
x_A & y_A & 1 \\
x_B & y_B & 1 \\
x_C & y_C & 1
\end{pmatrix}\neq 0.
$$

Cette condition signifie précisément que $A$, $B$ et $C$ ne sont pas
alignés.

Une fois $a$, $b$ et $c$ déterminés, on complète les carrés :

$$
\begin{aligned}
x^2+y^2+ax+by+c
&=\left(x+\frac a2\right)^2-\frac{a^2}{4}
  +\left(y+\frac b2\right)^2-\frac{b^2}{4}+c \\
&=0.
\end{aligned}
$$

Ainsi,

$$
\left(x+\frac a2\right)^2
+\left(y+\frac b2\right)^2
=\frac{a^2+b^2}{4}-c.
$$

Le centre et le rayon sont donc

$$
O=\left(-\frac a2,-\frac b2\right),
\qquad
R=\sqrt{\frac{a^2+b^2}{4}-c}.
$$

## Formulation homogène et déterminant

Les notes introduisent ensuite la forme homogène

$$
\alpha(x^2+y^2)+\beta x+\gamma y+\delta=0.
$$

Les coefficients ne sont définis qu'à un facteur multiplicatif non nul près.
Pour les trois points connus et un point variable $(x,y)$ du cercle, on écrit

$$
\begin{pmatrix}
x^2+y^2 & x & y & 1 \\
x_A^2+y_A^2 & x_A & y_A & 1 \\
x_B^2+y_B^2 & x_B & y_B & 1 \\
x_C^2+y_C^2 & x_C & y_C & 1
\end{pmatrix}
\begin{pmatrix}
\alpha \\
\beta \\
\gamma \\
\delta
\end{pmatrix}
=
\begin{pmatrix}
0 \\
0 \\
0 \\
0
\end{pmatrix}.
$$

Pour qu'une solution non nulle
$(\alpha,\beta,\gamma,\delta)$ existe, la matrice doit être singulière. Le
point $(x,y)$ appartient donc au cercle lorsque

$$
\det\begin{pmatrix}
x^2+y^2 & x & y & 1 \\
x_A^2+y_A^2 & x_A & y_A & 1 \\
x_B^2+y_B^2 & x_B & y_B & 1 \\
x_C^2+y_C^2 & x_C & y_C & 1
\end{pmatrix}=0.
$$

:::{note}
La formule $y=ax^2+bx+c$ apparaît brièvement puis est barrée dans les notes.
Elle décrit en général une parabole, pas un cercle ; elle n'est donc pas
retenue dans le raisonnement final.
:::

## Exemple : points $(0,0)$, $(0,1)$ et $(1,0)$

On considère

$$
A=(0,0),\qquad B=(1,0),\qquad C=(0,1).
$$

La formulation par déterminant donne

$$
\det\begin{pmatrix}
x^2+y^2 & x & y & 1 \\
0 & 0 & 0 & 1 \\
1 & 1 & 0 & 1 \\
1 & 0 & 1 & 1
\end{pmatrix}=0.
$$

En développant selon la première ligne, comme dans le cahier,

$$
\begin{aligned}
&(x^2+y^2)(1)-x(1)+y(-1)-1(0)=0, \\
&x^2+y^2-x-y=0.
\end{aligned}
$$

On complète séparément le carré en $x$ et le carré en $y$ :

$$
\begin{aligned}
0
&=x^2-x+y^2-y \\
&=x^2-2\left(\frac12\right)x
  +\left(\frac12\right)^2-\left(\frac12\right)^2 \\
&\quad
  +y^2-2\left(\frac12\right)y
  +\left(\frac12\right)^2-\left(\frac12\right)^2 \\
&=\left(x-\frac12\right)^2
  +\left(y-\frac12\right)^2
  -\left(\frac12\right)^2
  -\left(\frac12\right)^2.
\end{aligned}
$$

On en déduit

$$
\left(x-\frac12\right)^2
+\left(y-\frac12\right)^2
=\frac12.
$$

Le centre du cercle est donc

$$
O=\left(\frac12,\frac12\right),
$$

et son rayon vaut

$$
R=\sqrt{\frac12}=\frac{1}{\sqrt2}.
$$

## Fragment exponentiel figurant sur la première image

La première image contient un calcul distinct dont les variables ne sont pas
définies. Il part d'un seuil de $95\,\%$ :

$$
1-e^{-c\Delta t}=0{,}95.
$$

Les transformations manuscrites sont

$$
\begin{aligned}
1-e^{-c\Delta t}&=0{,}95, \\
e^{-c\Delta t}&=0{,}05, \\
-c\Delta t&=\ln(0{,}05), \\
c&=-\frac{\ln(0{,}05)}{\Delta t}, \\
c&=-\frac{\ln(5/100)}{\Delta t}, \\
c&=\frac{\ln(100/5)}{\Delta t}.
\end{aligned}
$$

:::{note}
**À vérifier :** aucun lien explicite avec la construction du cercle n'est
écrit sur la page. Ce calcul pourrait représenter une probabilité de succès ou
une loi d'approche exponentielle, mais le contexte manuscrit ne permet pas de
le déterminer avec certitude. Le schéma voisin et une matrice fortement barrée
sont trop ambigus pour être retranscrits sans invention.
:::
