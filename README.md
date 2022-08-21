[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.289)

# Compute network backbone
App to generate the backbone network from either a structural or functional network.

### Authors
- [Brad Caron](bacaron@utexas.edu)

### Contributors
- [Filipi N. Silva](https://filipinascimento.github.io)
- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)


### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)


### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2. Bassett, Danielle S., and Olaf Sporns. "Network neuroscience." Nature neuroscience 20, no. 3 (2017): 353. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)

3. M. A. Serrano et al. (2009) Extracting the Multiscale Backbone of Complex Weighted Networks. PNAS, 106:16, pp. 6483-6488. [https://doi.org/10.1073/pnas.0808904106](https://doi.org/10.1073/pnas.0808904106)

## Running the App

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.289](https://doi.org/10.25663/brainlife.app.289) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
    "network": "/input/network.json.gz",
    "parc": 0.05
}
```

3. Launch the App by executing 'main'

```bash
./main
```

The `filsilva/cxnetwork` ( [https://github.com/filipinascimento/cxnetworks-docker](https://github.com/filipinascimento/cxnetworks-docker) ) docker image is being used.

### Sample Datasets

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download
```

## Output

The main output of this App is a raw datatype containing all of the matrices generated, individual conmat dataytpes for count, length, density, and denlen, and a networkneuro datatypes for visualization.

#### Product.json

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.   

- Python3: https://www.python.org/downloads/
- igraph: https://igraph.org/python/
- jgf: https://pypi.org/project/jgf/
- tqdm: https://tqdm.github.io/

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University
