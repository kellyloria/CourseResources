## Question List

+ To what extent does population recovery of perennial plants after disturbances depend on stochastic germination processes versus site improvement by ruderal species?

+ Across a plant population, is more successful germination associated with reduced survivability due to energetic tradeoffs?

+ How do plant traits relevant to population establishment align or conflict with traits relevant to population persistence?

+ How relevant is local adaptation in highly asexual plant species?

+ How much of our understanding of local adaptation is biased by the types of species that we can easily study (e.g. prolific germinators)?

+ Do transplanted individuals (of the same genotype) that are germinated *ex situ* in greenhouses have the same development and survival trajectories as individuals that germinate *in situ*?

+ Do mixes of non-local populations perform better than single-origin populations when all of the populations are similarly unadapted to a given location?

+ What role do pollinators play in determining rates of plant outcrossing and selection of genotypes?

+ Does survival of a population depend more on interspecific interactions or intraspecific genetic composition?

+ To what extent is local adapation a result of coexistance with particular species versus selection by abiotic conditions?

+ Does the population structure of invasive species in their invaded range support or defy expectations based on genotype-environment associations in their native range?

## Chosen Question

**Does the population structure of invasive species in their invaded range support or defy expectations derived from genotype-environment associations in their native range?**

### Hypotheses related to diversity 

*Only some native populations escape outside their range and invasive populations proceed through a bottleneck into the invaded range. Therefore, invaded populations are less genetically diverse than native populations.*

<ul>
<span style="color:blue"><b>Prediction:</b></span> Both within-population and between-population diversity will be lower in invaded relative to native populations.
</ul>

<span style="color:blue"><b>Tests:</b></span> Perhaps some sort of ANOVA using F<sub>ST</sub> and F<sub>IS</sub> statistics 

&nbsp;

### Hypotheses related to GEAs

**Alternative #1:** *Genotype-environment associations establish relative positions of genotypes along an abiotic gradient regardless of the gradient range.*

<ul>
<span style="color:blue"><b>Prediction:</b></span> Invasive populations will represent a subset of the native populations and will be distributed hierarchically along environmental gradients as predicted by the native range GEA. Some invaded populations will correspond with different absolute locations along this gradient (i.e. adaptation is relative, not absolute) due to random absences of some genotypes in the invaded range.
</ul>

**Alternative #2:** *Genotype-environment associations determine absolute abiotic limits for a given genotype.*

<ul>
<span style="color:blue"><b>Prediction:</b></span> Genotypes will only occur in sites where environmental conditions match (in absolute terms) those of the native population that the invaded population is derived from.
</ul>

<span style="color:blue"><b>Tests:</b></span> Would initially need some sort of ordination of environmental variables to create 'gradients' for comparison. If testing for relative/hierarchical associatons with environment, would possibly look at something like NMDS to establish relative environment-adaptation potential of genotypes. By contrast, testing for genotype relationships with absolute environmental limits would require some sort of predictive modeling (maybe removing some individuals for validation) guided by the 'native' dataset. If you could generate a predictive model within the native distribution, you could then test whether that model is predictive across the invaded range.

### Other Hypotheses

*Invaded range facilitates population mixing that would not occur naturally in native range (e.g. genetically isolated populations of the native range that outcross in a new environment due to multiple introductions).* 

<ul>
<span style="color:blue"><b>Prediction:</b></span> Population structure in invaded range is distinct with a GEA pattern that is unrelated to GEA of native range. Either environmental conditions are outside of any conditions seen in native range (with a unique genetic population inhabiting this site) or several unique-to-native populations invade sites that fall within native environmental range but with unpredictable associations based on the 'mix-sources' of these invasive populations.
</ul>

<span style="color:blue"><b>Tests:</b></span> Definitely need some `STRUCTURE` analyses to determine level of 'unnatural' mixing within the invaded populations. If unique mixing is occurring within invaded range, you would need to develop some sort of composite variable that encapsulates mixed origins of populations so that you could use a GEA developed with native populations to predict locations of theoretical mixes (I have no idea if this is possible). You would then need some way to compare the predictive accuracy of the native GEA to a GEA derived only from invasive populations.  