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

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/be767d1a-58c5-476f-a118-1756c14b561f" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/f2cc30b8-e21b-4ce2-88f3-4b96f78329ae" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/6375710e-5da7-4325-bcba-b274c07c2adb" width="600">

- **RQ 02.** Qual a relação entre a maturidade do repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/0bdbb4dd-a0c1-4a48-a243-31741b05fb39" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/a52d331e-d7f9-45dc-bc79-dfd52ac5b18a" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/2e9cf8dc-91a2-42dc-aa7f-8d6eff3a1d48" width="600">

- **RQ 03.** Qual a relação entre a atividade dos repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/d12e288a-f50e-4de1-b9cd-496e7903672e" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/80f8f39d-4b0b-41bd-af2b-7e2978cbcb39" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/fc10facd-cdea-4065-b0d8-d796aedb2cc3" width="600">

- **RQ 04.** Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?

<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/8564d149-7932-4fe6-b6c8-f90afde47271" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/526e4044-5281-4c31-81bb-517fca0d24d7" width="600">
<img src="https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/62d9977b-628c-460f-8443-6be27e057dae" width="600">

