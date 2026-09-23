# Navier–Stokes incompressible et écoulement de Poiseuille

<div class="note-meta">
<p><strong>Domaines :</strong> mécanique des fluides, équations aux dérivées partielles, calcul tensoriel</p>
<p><strong>Synonymes :</strong> équations de Navier–Stokes, terme convectif, écoulement de Hagen–Poiseuille, écoulement en conduite</p>
<p><strong>Mots-clés :</strong> incompressibilité, divergence tensorielle, convection, profil parabolique, pression, viscosité, tube cylindrique</p>
</div>

Cette fiche part de la divergence du produit tensoriel
$\mathbf u\otimes\mathbf u$, relie les formes conservative et convective des
équations de Navier–Stokes, puis applique leur simplification à un écoulement
stationnaire pleinement développé dans un tube cylindrique.

Dans les notes, les notations $\mathbf u$ et $\mathbf v$ désignent toutes deux
le champ de vitesse. On emploie ici $\mathbf u$ pour le champ vectoriel et
$u(r)$ pour sa composante axiale.

## Du produit tensoriel au terme convectif

La divergence du produit tensoriel se développe selon l'identité

$$
\nabla\cdot(\mathbf u\otimes\mathbf u)
=\mathbf u\,(\nabla\cdot\mathbf u)
+(\mathbf u\cdot\nabla)\mathbf u.
$$

Pour retrouver cette identité composante par composante, on introduit une base
orthonormée $(\mathbf e_i)$ et on écrit

$$
\mathbf u=\sum_i u_i\mathbf e_i,
$$

ainsi que

$$
\nabla=\sum_j \mathbf e_j\frac{\partial}{\partial x_j}.
$$

Le produit tensoriel devient alors

$$
\begin{aligned}
\mathbf u\otimes\mathbf u
&=\left(\sum_i u_i\mathbf e_i\right)
  \otimes
  \left(\sum_j u_j\mathbf e_j\right) \\
&=\sum_{i,j}u_i u_j\,\mathbf e_i\otimes\mathbf e_j.
\end{aligned}
$$

Sa divergence s'obtient sans supprimer les étapes du développement indiciel :

$$
\begin{aligned}
\nabla\cdot(\mathbf u\otimes\mathbf u)
&=\left(\sum_k\mathbf e_k\frac{\partial}{\partial x_k}\right)
  \cdot
  \left(\sum_{i,j}u_i u_j\,\mathbf e_i\otimes\mathbf e_j\right) \\
&=\sum_{k,i,j}
  \frac{\partial(u_i u_j)}{\partial x_k}
  (\mathbf e_k\cdot\mathbf e_j)\,\mathbf e_i \\
&=\sum_{k,i}
  \frac{\partial(u_i u_k)}{\partial x_k}\,\mathbf e_i \\
&=\sum_{k,i}
  \left(
  u_i\frac{\partial u_k}{\partial x_k}
  +u_k\frac{\partial u_i}{\partial x_k}
  \right)\mathbf e_i \\
&=\left(\sum_k\frac{\partial u_k}{\partial x_k}\right)
  \left(\sum_i u_i\mathbf e_i\right)
  +\sum_i\left(\sum_k u_k\frac{\partial u_i}{\partial x_k}\right)\mathbf e_i \\
&=\mathbf u\,(\nabla\cdot\mathbf u)
  +(\mathbf u\cdot\nabla)\mathbf u.
\end{aligned}
$$

En notation indicielle, l'étape centrale est donc

$$
\frac{\partial(u_i u_j)}{\partial x_j}
=u_i\frac{\partial u_j}{\partial x_j}
+u_j\frac{\partial u_i}{\partial x_j}.
$$

## Continuité et incompressibilité

L'équation de continuité générale est

$$
\frac{\partial\rho}{\partial t}
+\nabla\cdot(\rho\mathbf u)=0.
$$

En développant la divergence,

$$
\frac{\partial\rho}{\partial t}
+\rho\,\nabla\cdot\mathbf u
+\mathbf u\cdot\nabla\rho=0.
$$

Lorsque la masse volumique est constante, les deux termes contenant ses
dérivées s'annulent. Il reste

$$
\nabla\cdot\mathbf u=0.
$$

L'identité précédente se réduit alors à

$$
\nabla\cdot(\mathbf u\otimes\mathbf u)
=(\mathbf u\cdot\nabla)\mathbf u.
$$

:::{note}
La mention manuscrite « $\rho\neq f(t)$ » semble indiquer que $\rho$ ne dépend
pas du temps. Cette seule hypothèse ne suffit pas à déduire
$\nabla\cdot\mathbf u=0$ si $\rho$ varie encore dans l'espace. La réduction
ci-dessus utilise donc l'hypothèse plus forte, cohérente avec la suite, d'une
masse volumique constante.
:::

## Équation de Navier–Stokes incompressible

La première page donne la forme suivante :

$$
\rho\frac{\partial\mathbf u}{\partial t}
+(\mathbf u\cdot\nabla)\mathbf u
=-\nabla p+\mu\Delta\mathbf u+\rho\mathbf g.
$$

:::{note}
**Correction probable :** le facteur $\rho$ semble manquer devant le terme
convectif dans cette ligne manuscrite. Pour un fluide newtonien incompressible
de masse volumique constante, la forme dimensionnellement cohérente est

$$
\rho\left(
\frac{\partial\mathbf u}{\partial t}
+(\mathbf u\cdot\nabla)\mathbf u
\right)
=-\nabla p+\mu\Delta\mathbf u+\rho\mathbf g.
$$
:::

La forme conservative associée s'écrit, lorsque $\rho$ est constante,

$$
\rho\frac{\partial\mathbf u}{\partial t}
+\rho\,\nabla\cdot(\mathbf u\otimes\mathbf u)
=-\nabla p+\mu\Delta\mathbf u+\rho\mathbf g.
$$

L'incompressibilité permet bien de passer de cette expression à la forme
convective.

## Cas spécial : écoulement pleinement développé dans un tube

On considère un tube cylindrique de rayon $R$, d'axe $x$. Le champ de vitesse
est supposé stationnaire, axisymétrique, unidirectionnel et pleinement
développé :

$$
\mathbf u=u(r)\,\mathbf e_x.
$$

Avec ces hypothèses,

$$
\frac{\partial\mathbf u}{\partial t}=0,
$$

et le terme convectif s'annule :

$$
\begin{aligned}
(\mathbf u\cdot\nabla)\mathbf u
&=u(r)\frac{\partial}{\partial x}
  \left(u(r)\mathbf e_x\right) \\
&=0.
\end{aligned}
$$

En négligeant la force volumique, ou en l'intégrant dans la pression, la
composante axiale de Navier–Stokes devient

$$
\frac{1}{r}\frac{d}{dr}
\left(r\frac{du}{dr}\right)
=\frac{1}{\mu}\frac{dp}{dx}.
$$

### Intégration du profil de vitesse

On multiplie d'abord par $r$ :

$$
\frac{d}{dr}\left(r\frac{du}{dr}\right)
=\frac{r}{\mu}\frac{dp}{dx}.
$$

Une première intégration donne

$$
r\frac{du}{dr}
=\frac{r^2}{2\mu}\frac{dp}{dx}+C_1.
$$

On divise par $r$ :

$$
\frac{du}{dr}
=\frac{r}{2\mu}\frac{dp}{dx}+\frac{C_1}{r}.
$$

Une deuxième intégration conduit à

$$
u(r)
=\frac{r^2}{4\mu}\frac{dp}{dx}
+C_1\ln r+C_2.
$$

La vitesse doit rester finie sur l'axe $r=0$. Le terme $\ln r$ impose donc

$$
C_1=0.
$$

En notant la vitesse sur l'axe $V_0=u(0)$, on obtient

$$
C_2=V_0.
$$

La condition d'adhérence à la paroi est

$$
u(R)=0.
$$

Elle donne successivement

$$
\begin{aligned}
0
&=\frac{R^2}{4\mu}\frac{dp}{dx}+V_0, \\
V_0
&=-\frac{R^2}{4\mu}\frac{dp}{dx}.
\end{aligned}
$$

Le profil final est donc

$$
\begin{aligned}
u(r)
&=\frac{r^2}{4\mu}\frac{dp}{dx}+V_0 \\
&=\frac{1}{4\mu}\frac{dp}{dx}\left(r^2-R^2\right).
\end{aligned}
$$

Lorsque la pression décroît dans le sens de l'écoulement,
$dp/dx<0$, cette expression donne bien $u(r)>0$ pour $0\leq r<R$.

## Calcul de moyenne présent dans les notes

Les notes définissent la moyenne par

$$
\overline u_{\mathrm{notes}}
=\frac{1}{R}\int_0^R u(r)\,dr.
$$

En remplaçant le profil parabolique, le calcul manuscrit se déroule ainsi :

$$
\begin{aligned}
\overline u_{\mathrm{notes}}
&=\frac{1}{R}\int_0^R
  \frac{1}{4\mu}\frac{dp}{dx}\left(r^2-R^2\right)\,dr \\
&=\frac{1}{4R\mu}\frac{dp}{dx}
  \int_0^R\left(r^2-R^2\right)\,dr \\
&=\frac{1}{4R\mu}\frac{dp}{dx}
  \left[\frac{r^3}{3}-R^2r\right]_0^R \\
&=\frac{1}{4R\mu}\frac{dp}{dx}
  \left(\frac{R^3}{3}-R^3\right) \\
&=\frac{1}{4R\mu}\frac{dp}{dx}
  \left(-\frac{2R^3}{3}\right) \\
&=-\frac{R^2}{6\mu}\frac{dp}{dx} \\
&=\frac{2}{3}V_0.
\end{aligned}
$$

:::{note}
**Point géométrique à corriger :** $R^{-1}\int_0^R u(r)\,dr$ est une
moyenne le long d'un rayon, et non la vitesse moyenne sur la section d'un tube
cylindrique. La moyenne surfacique doit tenir compte de l'élément d'aire
$dA=2\pi r\,dr$ :

$$
\begin{aligned}
\overline u
&=\frac{1}{\pi R^2}\int_A u\,dA \\
&=\frac{2}{R^2}\int_0^R u(r)\,r\,dr \\
&=\frac{2}{R^2}\int_0^R
  \frac{1}{4\mu}\frac{dp}{dx}(r^2-R^2)r\,dr \\
&=\frac{1}{2\mu R^2}\frac{dp}{dx}
  \left[\frac{r^4}{4}-\frac{R^2r^2}{2}\right]_0^R \\
&=-\frac{R^2}{8\mu}\frac{dp}{dx} \\
&=\frac{V_0}{2}.
\end{aligned}
$$
:::

## Relation isolée en tête de la troisième page

Une relation de conservation, non réutilisée dans le calcul de Poiseuille,
figure en haut de la dernière page. Sa lecture probable est

$$
V\frac{\partial(\rho h)}{\partial t}
+\nabla(\xi\mathbf q)=S_V.
$$

:::{note}
**À vérifier :** les symboles $\xi$, $\mathbf q$ et $S_V$, ainsi que
l'opérateur placé devant $\xi\mathbf q$, sont difficiles à distinguer sur
l'image. Cette relation est conservée ici pour ne pas perdre le fragment
manuscrit, mais son lien avec le reste de la fiche n'est pas explicite.
:::
