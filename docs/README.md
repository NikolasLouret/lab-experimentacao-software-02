# Relatório

Relatório final para o laboratório de estudo das características de qualidade de sistemas Java

## Introdução

No processo de desenvolvimento de sistemas open-source, em que diversos desenvolvedores contribuem em partes diferentes do código, um dos riscos a serem gerenciados diz respeito à evolução dos seus atributos de qualidade interna. Isto é, ao se adotar uma abordagem colaborativa, corre-se o risco de tornar vulnerável aspectos como modularidade, manutenabilidade, ou legibilidade do software produzido. Para tanto, diversas abordagens modernas buscam aperfeiçoar tal processo, através da adoção de práticas relacionadas à revisão de código ou à análise estática através de ferramentas de CI/CD.

Neste contexto, o objetivo deste laboratório é analisar aspectos da qualidade de repositórios desenvolvidos na linguagem Java, correlacionado-os com características do seu processo de desenvolvimento, sob a perspectiva de métricas de produto calculadas através da ferramenta [CK](https://github.com/mauricioaniche/ck).

## Hipóteses Informais

- **RQ 01.** Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?

Hipótese: Repositórios mais populares, medidos pelo número de estrelas, tendem a ter características de qualidade superiores, como menor acoplamento entre objetos (CBO), uma árvore de herança menos profunda (DIT) e maior coesão entre métodos (LCOM). A popularidade pode indicar confiança dos desenvolvedores na qualidade do código.

- **RQ 02.** Qual a relação entre a maturidade do repositórios e as suas características de qualidade?

Hipótese: Repositórios mais antigos, indicando maior maturidade, tendem a apresentar características de qualidade mais elevadas. A experiência acumulada ao longo do tempo pode levar a melhores práticas de desenvolvimento, resultando em um código com menor acoplamento, menor profundidade de herança e maior coesão entre métodos.

- **RQ 03.** Qual a relação entre a atividade dos repositórios e as suas características de qualidade?

Hipótese: Repositórios com maior atividade, medida pelo número de releases, tendem a apresentar características de qualidade superiores. A atividade contínua pode indicar uma comunidade ativa de desenvolvedores, resultando em correções rápidas, melhorias constantes e, consequentemente, um código com menor acoplamento, menor profundidade de herança e maior coesão entre métodos.

- **RQ 04.** Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?

Hipótese: Repositórios com um maior volume de código, medido pelas linhas de código (LOC) e linhas de comentários, tendem a apresentar características de qualidade inferiores. Um código extenso pode indicar maior complexidade, dificultando a manutenção e aumentando a probabilidade de problemas de qualidade, como acoplamento excessivo. Portanto, espera-se que um código mais enxuto, com menos linhas de código e comentários, apresente uma melhor qualidade em termos de menor acoplamento entre objetos, menor profundidade na árvore de herança e maior coesão entre métodos.

## Resultados Obtidos

- **RQ 01.** Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/935c5618-6420-4572-ac7e-ab493719b737" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/3078cf35-721b-44ea-a5de-133448c7b19b" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/5fd21a1c-1931-4ba6-adf9-6fcd919b3d08" width="600">

- **RQ 02.** Qual a relação entre a maturidade do repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/77a53a39-19e1-4821-8f9b-78f6370bbcf9" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/6f81a21b-2ecc-4f18-b333-0827a095b87c" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/4a6dbc1f-6c18-4b26-b02a-5ec9fcf78134" width="600">

- **RQ 03.** Qual a relação entre a atividade dos repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/f37df97b-3f8e-4e77-9d41-bbd634109c9c" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/42cf9bf0-8d44-4931-973c-1f83ce37c35b" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/f22e4c9b-d1d4-4e52-82b6-d3dad2291f45" width="600">

- **RQ 04.** Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/c42a6d0a-44f3-47e7-8ee5-71c511525593" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/09f2a1a3-687f-4c5f-b480-1d7446528fec" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/a9482f71-93ea-482b-b04c-6fe3db1cf4d6" width="600">
