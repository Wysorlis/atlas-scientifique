# Discrétisation explicite et implicite d’un filtre du premier ordre

<div class="note-meta">
  <div><strong>Domaines :</strong> analyse numérique, automatique, traitement du signal</div>
  <div><strong>Synonymes :</strong> filtre passe-bas du premier ordre, schéma d’Euler explicite, schéma d’Euler implicite</div>
  <div><strong>Mots-clés :</strong> filtre, constante de temps, discrétisation temporelle, stabilité, récurrence</div>
</div>

On considère le filtre différentiel du premier ordre

$$
\boxed{
\tau\frac{\mathrm dy}{\mathrm dt}+y=u
},
$$

où $u(t)$ est l’entrée, $y(t)$ la sortie et $\tau>0$ la constante de
temps. Les notes comparent deux manières de calculer la sortie aux instants
$t_n=n\Delta t$.

## Schéma explicite

Dans le schéma d’Euler explicite, la dérivée est approchée entre $t_n$ et
$t_{n+1}$, tandis que les autres termes sont évalués à l’instant $t_n$ :

$$
\tau\frac{y^{n+1}-y^n}{\Delta t}+y^n=u^n.
$$

On isole progressivement $y^{n+1}$ :

$$
\begin{aligned}
\tau\frac{y^{n+1}-y^n}{\Delta t}
&=u^n-y^n,\\
y^{n+1}-y^n
&=\frac{\Delta t}{\tau}(u^n-y^n),\\
y^{n+1}
&=y^n+\frac{\Delta t}{\tau}(u^n-y^n).
\end{aligned}
$$

Le résultat peut aussi s’écrire comme dans la page manuscrite :

$$
\boxed{
y^{n+1}
=y^n+\frac{u^n-y^n}{\tau/\Delta t}
}.
$$

En posant

$$
\lambda=\frac{\Delta t}{\tau},
$$

la mise à jour prend la forme

$$
y^{n+1}=(1-\lambda)y^n+\lambda u^n.
$$

Lorsque $0\leq\lambda\leq1$, la nouvelle valeur est une moyenne pondérée de
$y^n$ et de $u^n$. Si $\Delta t$ devient plus grand que $\tau$, le poids de
$y^n$ devient négatif : la réponse numérique commence à osciller.

## Schéma implicite

Dans le schéma d’Euler implicite, les termes non différentiels sont évalués à
l’instant $t_{n+1}$ :

$$
\tau\frac{y^{n+1}-y^n}{\Delta t}+y^{n+1}=u^{n+1}.
$$

On développe puis on regroupe les termes en $y^{n+1}$ :

$$
\begin{aligned}
\frac{\tau}{\Delta t}(y^{n+1}-y^n)+y^{n+1}
&=u^{n+1},\\
\frac{\tau}{\Delta t}y^{n+1}
-\frac{\tau}{\Delta t}y^n
+y^{n+1}
&=u^{n+1},\\
y^{n+1}\left(\frac{\tau}{\Delta t}+1\right)
&=u^{n+1}+\frac{\tau}{\Delta t}y^n,\\
y^{n+1}
&=\frac{u^{n+1}+\dfrac{\tau}{\Delta t}y^n}
{1+\dfrac{\tau}{\Delta t}}.
\end{aligned}
$$

Pour retrouver une écriture incrémentale, on soustrait et on ajoute $y^n$ au
numérateur :

$$
\begin{aligned}
y^{n+1}
&=\frac{
u^{n+1}-y^n
y^n+\dfrac{\tau}{\Delta t}y^n
}{1+\dfrac{\tau}{\Delta t}}\\
&=\frac{u^{n+1}-y^n}
{1+\dfrac{\tau}{\Delta t}}
+y^n.
\end{aligned}
$$

On obtient donc

$$
\boxed{
y^{n+1}
=y^n+
\frac{u^{n+1}-y^n}
{1+\tau/\Delta t}
}.
$$

En utilisant à nouveau $\lambda=\Delta t/\tau$,

$$
y^{n+1}
=\frac{1}{1+\lambda}y^n
+\frac{\lambda}{1+\lambda}u^{n+1}.
$$

Les deux coefficients sont positifs et leur somme vaut $1$, quelle que soit la
valeur positive de $\Delta t$.

## Comparaison de la stabilité

Pour observer uniquement l’amortissement numérique, supposons l’entrée $u$
constante et posons l’erreur $e^n=y^n-u$.

### Euler explicite

$$
e^{n+1}
=\left(1-\frac{\Delta t}{\tau}\right)e^n.
$$

La stabilité exige

$$
\left|1-\frac{\Delta t}{\tau}\right|<1,
$$

soit

$$
0<\frac{\Delta t}{\tau}<2.
$$

La convergence reste monotone seulement si

$$
0<\frac{\Delta t}{\tau}\leq1.
$$

Cette condition explique l’avertissement entouré dans les notes lorsque
$\tau<\Delta t$.

### Euler implicite

$$
e^{n+1}
=\frac{\tau}{\tau+\Delta t}e^n.
$$

Pour $\tau>0$ et $\Delta t>0$,

$$
0<\frac{\tau}{\tau+\Delta t}<1.
$$

Le schéma implicite amortit donc l’erreur sans oscillation pour tout pas de
temps positif.

## Formules à retenir

| Schéma | Mise à jour |
|---|---|
| Explicite | $\displaystyle y^{n+1}=y^n+\frac{\Delta t}{\tau}(u^n-y^n)$ |
| Implicite | $\displaystyle y^{n+1}=y^n+\frac{u^{n+1}-y^n}{1+\tau/\Delta t}$ |

Le schéma explicite est direct, mais impose de contrôler le rapport
$\Delta t/\tau$. Le schéma implicite demande de manipuler la valeur au nouvel
instant, mais il conserve ici une mise à jour explicite après résolution de
l’équation algébrique et reste stable pour tout $\Delta t>0$.

~~~{note}
Une annotation isolée au bas de la page semble introduire une suite de
constantes de temps $\tau_n$, mais les indices et l’exposant ne sont pas assez
lisibles pour en donner une transcription fiable. Elle n’intervient pas dans
la comparaison des deux schémas ci-dessus.
~~~

