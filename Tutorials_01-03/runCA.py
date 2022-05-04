# import CodeAster
import code_aster
from code_aster.Commands import *

# initialize
code_aster.init(LANG='EN')

# create and read mesh
monMaillage = code_aster.Mesh()
monMaillage.readMedFile("_ExportedFromSalomeObject_0_1_2_3.med")

# prepare model
monModel = code_aster.Model(monMaillage)
monModel.addModelingOnMesh(code_aster.Physics.Mechanics, code_aster.Modelings.Tridimensional)
monModel.build()

# material settings
matProp = code_aster.MaterialProperty("ELAS")
matProp.addPropertyReal("E", 210000, True)
matProp.addPropertyReal("NU", 0.3, True)

steel = code_aster.Material()
steel.addMaterialProperty(matProp)
steel.build()

fieldmat = code_aster.MaterialField(monMaillage)
fieldmat.addMaterialsOnGroupOfCells(steel, ["beam"])
fieldmat.buildWithoutExternalStateVariables()

# create boundary conditions
bc_dirichlet = code_aster.MechanicalDirichletBC(monModel)
bc_dirichlet.addBCOnNodes(code_aster.PhysicalQuantityComponent.Dx, 0.0, "fix")
bc_dirichlet.addBCOnNodes(code_aster.PhysicalQuantityComponent.Dy, 0.0, "fix")
bc_dirichlet.addBCOnNodes(code_aster.PhysicalQuantityComponent.Dz, 0.0, "fix")
bc_dirichlet.build()

load = code_aster.ForceReal()
load.setValue(code_aster.PhysicalQuantityComponent.Fy, -10)

bc_load = code_aster.ForceOnFaceReal(monModel)
bc_load.setValue(load, "force")
bc_load.build()

# linear solver
mongolver = code_aster.MumpsSolver(code_aster.Renumbering.Metis)

# set up analysis
mecaStatique = code_aster.LinearStaticAnalysis(monModel, fieldmat)
mecaStatique.addDirichletBC(bc_dirichlet)
mecaStatique.addLoad(bc_load)
mecaStatique.setLinearSolver(mongolver)

# run the analysis
resu = mecaStatique.execute()

# print the results
resu.printMedFile("cantilever.rmed")

# finalize
code_aster.close()
