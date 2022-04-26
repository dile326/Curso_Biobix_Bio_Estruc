# Comparative modeling by the AutoModel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the AutoModel class

log.verbose()    # request verbose output
env = Environ()  # create a new MODELLER environment to build this model in

env.io.hetatm = True

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = AutoModel(env,
              alnfile  = '',     # alignment filename
              knowns   = '',              # codes of the templates
              sequence = '')              # code of the target
a.starting_model=                  # index of the first model
a.ending_model  =                  # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling