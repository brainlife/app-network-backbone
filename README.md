<h1 align="center">Compute Network Backbone</h1>

<p align="center">
  The statistically significant backbone of a weighted structural or functional brain network, extracted with the disparity filter.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.665"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.665-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

> 📍 **This branch, `v1.0`, is the brainlife.io App Compute Network Backbone** ([doi:10.25663/brainlife.app.665](https://doi.org/10.25663/brainlife.app.665)).

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Extracts the backbone of a weighted structural or functional connectivity network with the disparity filter (Serrano et al. 2009) using networkx and igraph, keeping only statistically significant edges.**

Loads the first network from a JGF network file, computes a disparity-filter significance score (alpha) for every weighted edge and keeps edges whose alpha is below the alpha parameter, saving the backbone as output/network.json.gz. Use it to sparsify dense connectivity matrices before network analysis; edges at nodes with a single connection never pass the cut in the undirected case.

| | |
|---|---|
| 📥 **Inputs** | `generic/network` |
| 📤 **Outputs** | `generic/network` |
| 🐳 **Container** | `brainlife/python-networks` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.665](https://doi.org/10.25663/brainlife.app.665) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `network` | `generic/network` | yes | Weighted network in JGF format (network.json.gz); only the first network in the file is used. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `generic/network` | Backbone network (network.json.gz) containing only the edges that pass the disparity-filter threshold. |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `alpha` | number | `0.05` | Disparity-filter significance threshold: an edge is kept when its alpha score is below this value (smaller keeps fewer edges). |

</details>

<!-- brainlife-app:end -->

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.665](https://doi.org/10.25663/brainlife.app.665), choose a `generic/network` dataset (a weighted network in JGF format) from your project, set `alpha` and press **Execute**. The result is a `generic/network` dataset tagged `backbone`, archived to your project for further network analysis.

The App:

1. loads the first network in the JGF file (`network.json.gz`) and converts it to a NetworkX graph;
2. computes the disparity-filter significance score (alpha) of every weighted edge (Serrano et al. 2009);
3. keeps only edges whose alpha is below the `alpha` threshold (default `0.05`; smaller values keep fewer edges);
4. saves the backbone back to JGF.

The disparity-filter code is adapted from [aekpalakorn/python-backbone-network](https://github.com/aekpalakorn/python-backbone-network).

### 💻 Locally

You need [Singularity/Apptainer](https://apptainer.org/). Python, NetworkX, igraph, [jgf](https://pypi.org/project/jgf/) and tqdm run inside the `brainlife/python-networks` container.

1. Clone this repository and check out the branch brainlife.io runs: `git checkout v1.0`.
2. Create `config.json` with the path to your network and the threshold:

   ```json
   {
       "network": "/input/network/network.json.gz",
       "alpha": 0.05
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

### 🧪 Sample data

Download sample datasets from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download <dataset-id>
```

## 📦 Outputs

```text
output/
└── network.json.gz   backbone network (JGF) with only the edges that pass the alpha threshold
```

## 🩺 Troubleshooting

- **Nodes lose all their edges**: in undirected networks, edges of nodes with a single connection never receive an alpha score and are dropped. Raise `alpha` to keep more of the network.
- **Only part of a multi-network file is processed**: the App uses only the first network in the JGF file.

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Serrano MA, Boguñá M, Vespignani A. Extracting the multiscale backbone of complex weighted networks. *PNAS* 106(16):6483–6488 (2009). [doi:10.1073/pnas.0808904106](https://doi.org/10.1073/pnas.0808904106)
- Bassett DS, Sporns O. Network neuroscience. *Nature Neuroscience* 20(3):353 (2017). [doi:10.1038/nn.4502](https://doi.org/10.1038/nn.4502)
- Compute Network Backbone. brainlife.io App. [doi:10.25663/brainlife.app.665](https://doi.org/10.25663/brainlife.app.665)
- Serrano MA, Boguna M, Vespignani A. Extracting the multiscale backbone of complex weighted networks. PNAS 106(16):6483-6488 (2009).
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## 👥 Authors

- Brad Caron

**Contributors:** [Filipi N. Silva](https://filipinascimento.github.io), Franco Pestilli

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

[MIT](LICENSE).
