# code-aster-examples
A number of examples for the open-source Finite Element Solver [Code_Aster](https://www.code-aster.org/) and [Salome_Meca](https://www.code-aster.org/spip.php?article303)

## Examples

Each folder contains a `.med` file with the mesh of the structure and a `.comm` file with the command file for Code_Aster. With these files anyone shoulf be able to reproduce the analyses with or without Salome_Meca. See the [IFC2CA video](https://youtu.be/V9Pc7SJvuRg) if you want to see how to reproduce the analyses with asterStudy, a dedicated module of Salome_Meca.

[Tutorials 01-03](Tutorials_01-03): Static analysis of a cantilever beam with 3D solid elements and post-processing of results
- [Video - Tutorial 01](https://youtu.be/lFUF5EelFUo)
- [Video - Tutorial 02](https://youtu.be/BizOXE3T9m8)
- [Video - Tutorial 03](https://youtu.be/07UxN1EaUvI)


[Tutorials 04-06](Tutorials_04-06): Steady-state thermo-mechanical analysis of a cantilever beam with 3D solid elements
- [Video - Tutorial 04](https://youtu.be/Rs_DuxT5dgw)
- [Video - Tutorial 05](https://youtu.be/D7V7Qn-40DU)
- [Video - Tutorial 06](https://youtu.be/eXNyT-aPh6Y)

[Tutorial 07](Tutorial_07): Static analysis of a cantilever beam with beam elements and post-processing of results
- [Video](https://youtu.be/Cx6mGyJH1Ms)

Tutorial 08: Static analysis of a cantilever beam with shell elements and post-processing of results
- [Video](https://youtu.be/qror21Uzc6c)

[Tutorial 09](Tutorial_09): Calculation of reinforcement density for shell elements
- [Video](https://youtu.be/wo5SJwPJCfU)

[Tutorial 10 - Connect Non-Conformal Meshes](Tutorial_10): Connect non-conformal meshes, that is, meshes with interface boundaries in which the mesh node locations are not identical.
- [Video](https://youtu.be/4peRNehSsj4)

[Tutorial 11 - Connect Conformal Meshes](Tutorial_11): Connect conformal meshes, that is, meshes with interface boundaries in which the mesh node locations are identical.
- [Video](https://youtu.be/U4qTv7UFFdA)

[Tutorial 12 - Connect Objects With "Partition" Command](Tutorial_12): Use of the "partition" command in GEOM module of Salome_Meca to connect objects and obtain a single object to be meshed, similarly to "Union" operation in other software.
- [Video](https://youtu.be/pdlUbAUb1GY)

[Tutorial 13 - Modal Analysis with Solid Elements](Tutorial_13): perform a modal analysis of a 3D model with solid elements.
- [Video](https://youtu.be/qnE_PcYbw7M)

[Define Local Axes for 1D Elements](DefineLocalAxes1D): Define the orientation of the local axes of 1D elements in Code_Aster and extract this information in the result file, then visualize the local axes in Paraview
- [Video](https://youtu.be/FUiFjAtCyX0)

[Define Custom Beam Profile](CustomBeamProfile): Define a custom profile for beam elements given that these properties are calculated beforehand or extracted from a table. Extract not only the generalized forces but also the maximum stresses for each type of response
- [Video](https://youtu.be/uZBcvgoby54)

[Composite Shells](CompositeShellExample): Define a composite shell with an arbitrary number of layers, orhtotropic materials and arbitrary material directions and extract generalized forces and stress for a specific layer. BONUS: Example is performed with a Cross Laminated Timber (CLT) panel
- [Video](https://youtu.be/52INSrQ48iQ)

[Parametric Study](ParametricStudyExample): Setup and perform a parametric analysis based on the composite shell example and by modifying the orientation of the layers of the panel from an initial angle of 0 to a final angle of 90 degrees with a step of 10. This tutorial is based on modifying the command file with python outside the asterStudy module. It does not cover the case of a parametric geometry.
- [Video](https://youtu.be/Fy49b0nwpXI)

[Tensegrity Structure Example](TensegrityExample): Nonlinear dynamic analysis of a tensegrity structure with Code_Aster
- [Simulation Video](https://youtu.be/PegRyW-5HXY)

[Tensegrity Structure Seismic Example](TensegritySeismic): Nonlinear dynamic analysis of a tensegrity structure under ground excitation with Code_Aster
- [Simulation Video](https://youtu.be/mPJh2J6BfA8)

[IFC2CA Portal Example](IFC2CA_PortalExample): Download the IFC2CA example files and load them in Salome_Meca. Here you can find the files for the portal_01 example

_Note: The repository referenced in the video has been moved in the [IfcOpenShell/analysis-models](https://github.com/IfcOpenShell/analysis-models) repository_
- [Video](https://youtu.be/V9Pc7SJvuRg)

[Rod Example](RodExample): Perform a multi-step static analysis with material and geometric nonlinearity, using an elasto-plastic material model with kinematic hardening and a logarithmic strain for geometric nonlinearity in large deformations.
Moreover, use a Jupyter Lab notebook to do some basic pre- and post-processing based on the input and output files.
- [Video](https://youtu.be/3z35NDNWV78)

[Linear Dynamic Analysis Example](LDA-Example): Run a linear transient dynamic analysis of a building structure based on an acceleration ground-motion time-history, after performing a modal analysis and assigning a classical damping matrix based on user-defined damping ratios for each mode.
Moreover, use a Jupyter Lab notebook to do some basic post-processing based on the output test files that are created.
- [Video](https://youtu.be/QoaNW4zC5u0)

[Linear Dynamic Analysis Example with Modal Base](LDA-Modal-Example): Run a linear transient dynamic analysis of a building structure based on an acceleration ground-motion time-history, using a modal base of the structure; that is the mode shapes from a modal analysis. Modify the input file with respect to the standard dynamic analysis that uses a physical base to define the modal base, assign a classical damping matrix based on damping ratios for each mode, and restore back the results from the modal to the physical base, in order to extract the displacement time-histories in an external 'resu' file.
- [Video](https://youtu.be/faFMYlkHM0g)

## License
All content is licensed under an open-source, 'copyleft' license:
[Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
![Attribution-ShareAlike 4.0 International](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)
