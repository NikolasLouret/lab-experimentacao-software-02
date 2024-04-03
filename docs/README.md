# Relatório

Relatório final para o laboratório de estudo das características de qualidade de sistemas Java

## Introdução

No processo de desenvolvimento de sistemas open-source, em que diversos desenvolvedores contribuem em partes diferentes do código, um dos riscos a serem gerenciados diz respeito à evolução dos seus atributos de qualidade interna. Isto é, ao se adotar uma abordagem colaborativa, corre-se o risco de tornar vulnerável aspectos como modularidade, manutenabilidade, ou legibilidade do software produzido. Para tanto, diversas abordagens modernas buscam aperfeiçoar tal processo, através da adoção de práticas relacionadas à revisão de código ou à análise estática através de ferramentas de CI/CD.

Neste contexto, o objetivo deste laboratório é analisar aspectos da qualidade de repositórios desenvolvidos na linguagem Java, correlacionado-os com características do seu processo de desenvolvimento, sob a perspectiva de métricas de produto calculadas através da ferramenta [CK](https://github.com/mauricioaniche/ck).

## Hipóteses Informais

-   **RQ 01.** Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?

Hipótese: Repositórios mais populares, medidos pelo número de estrelas, tendem a ter características de qualidade superiores, como menor acoplamento entre objetos (CBO), uma árvore de herança menos profunda (DIT) e maior coesão entre métodos (LCOM). A popularidade pode indicar confiança dos desenvolvedores na qualidade do código.

-   **RQ 02.** Qual a relação entre a maturidade do repositórios e as suas características de qualidade?

Hipótese: Repositórios mais antigos, indicando maior maturidade, tendem a apresentar características de qualidade mais elevadas. A experiência acumulada ao longo do tempo pode levar a melhores práticas de desenvolvimento, resultando em um código com menor acoplamento, menor profundidade de herança e maior coesão entre métodos.

-   **RQ 03.** Qual a relação entre a atividade dos repositórios e as suas características de qualidade?

Hipótese: Repositórios com maior atividade, medida pelo número de releases, tendem a apresentar características de qualidade superiores. A atividade contínua pode indicar uma comunidade ativa de desenvolvedores, resultando em correções rápidas, melhorias constantes e, consequentemente, um código com menor acoplamento, menor profundidade de herança e maior coesão entre métodos.

-   **RQ 04.** Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?

Hipótese: Repositórios com um maior volume de código, medido pelas linhas de código (LOC) e linhas de comentários, tendem a apresentar características de qualidade inferiores. Um código extenso pode indicar maior complexidade, dificultando a manutenção e aumentando a probabilidade de problemas de qualidade, como acoplamento excessivo. Portanto, espera-se que um código mais enxuto, com menos linhas de código e comentários, apresente uma melhor qualidade em termos de menor acoplamento entre objetos, menor profundidade na árvore de herança e maior coesão entre métodos.

## Resultados Obtidos

A seção de Resultados Obtidos do presente trabalho apresenta uma análise das relações entre métricas de qualidade de código (CBO, DIT, LCOM) e a popularidade, maturidade, atividade e tamanho dos repositórios Java, medido pelo número de estrelas, ano de criação do repositório, número de releases lançadas e o número de linhas de código (LOC), respectivamente.

-   **RQ 01.** Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?
    | | |
    | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ![Gráfico 1 (CBO × Popularidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/be767d1a-58c5-476f-a118-1756c14b561f) | ![Gráfico 2 (DIT × Popularidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/f2cc30b8-e21b-4ce2-88f3-4b96f78329ae) |
    | ![Gráfico 3 (LCOM × Popularidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/6375710e-5da7-4325-bcba-b274c07c2adb) | ![Gráfico 4 (Heatmap Popularidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/77488551/88006761-bf3b-4957-a28f-a978a944585a) |

**<h4 align="center">Coeficiente de Spearman</h4>**

<div align="center" style="display:flex;">
    
|         | CBO   | DIT Máx                | LCOM  |
| :------ | :---- | :--------------------- | :---- |
| ρ (rho) | 0.05  | 0.14                   | 0.07  |
| p-value | 0.102 | 1.66 × 10<sup>-5</sup> | 0.037 |

</div>

A análise dos gráficos referentes às métricas CK do CBO, DIT e LCOM em relação à popularidade dos repositórios Java revela informações interessantes sobre a relação entre qualidade e atratividade para a comunidade de desenvolvedores. Inicialmente, não foi identificada uma correlação direta entre essas métricas e a popularidade dos repositórios, como evidenciado pelos valores de _p-value_ e coeficiente de correlação (_ρ_).

No caso do CBO, apesar de não haver uma correlação significativa com a popularidade, observou-se uma variabilidade considerável no número de estrelas para repositórios com CBO alto, indicando que fatores como utilidade do projeto, qualidade da documentação e engajamento da comunidade podem ter maior impacto na popularidade do que o próprio CBO.

Quanto ao DIT, embora tenha sido identificada uma correlação estatisticamente significativa, esta foi fraca e negativa. A dispersão dos pontos no gráfico também sugere que outros fatores além do DIT influenciam a popularidade, como a utilidade do projeto e a qualidade da documentação.

Por fim, assim como no CBO, a análise do LCOM mostrou não existir correlação entre essa métrica e a popularidade.

A hipótese inicial de que repositórios mais populares tendem a ter características de qualidade superiores não foi totalmente confirmada pelos dados analisados. Embora existam correlações estatísticas em algumas métricas, como DIT, a força dessas correlações é insignificante, e a grande dispersão dos dados sugere a influência de múltiplos fatores na popularidade dos repositórios. Portanto, a relação entre a popularidade dos repositórios e suas características de qualidade não é direta nem linear.

-   **RQ 02.** Qual a relação entre a maturidade do repositórios e as suas características de qualidade?
    | | |
    | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ![Gráfico 5 (CBO × Maturidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/0bdbb4dd-a0c1-4a48-a243-31741b05fb39) | ![Gráfico 6 (DIT × Maturidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/a52d331e-d7f9-45dc-bc79-dfd52ac5b18a) |
    | ![Gráfico 7 (LCOM × Maturidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/2e9cf8dc-91a2-42dc-aa7f-8d6eff3a1d48) | ![Gráfico 8 (Heatmap Maturidade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/77488551/05312102-5772-4171-9f0e-3be24b0c5255) |

**<h4 align="center">Coeficiente de Spearman</h4>**

<div align="center" style="display:flex;">

|         | CBO    | DIT Máx                   | LCOM                      |
| :------ | :----- | :------------------------ | :------------------------ |
| ρ (rho) | 0.02   | 0.3                       | 0.23                      |
| p-value | 0.5299 | 7.5789 × 10<sup>-21</sup> | 1.9075 × 10<sup>-12</sup> |

</div>

A análise dos gráficos referentes às métricas CK do CBO, DIT e LCOM em relação à popularidade dos repositórios Java revela informações interessantes sobre a relação entre qualidade e atratividade para a comunidade de desenvolvedores. Inicialmente, não foi identificada uma correlação direta entre essas métricas e a popularidade dos repositórios, como evidenciado pelos valores de _p-value_ e coeficiente de correlação (_ρ_).

No caso do CBO, apesar de não haver uma correlação significativa com a popularidade, observou-se uma variabilidade considerável no número de estrelas para repositórios com CBO alto, indicando que fatores como utilidade do projeto, qualidade da documentação e engajamento da comunidade podem ter maior impacto na popularidade do que o próprio CBO.

Quanto ao DIT, embora tenha sido identificada uma correlação estatisticamente significativa, esta foi fraca e negativa. A dispersão dos pontos no gráfico também sugere que outros fatores além do DIT influenciam a popularidade, como a utilidade do projeto e a qualidade da documentação.

Por fim, assim como no CBO, a análise do LCOM mostrou não existir correlação entre essa métrica e a popularidade.

A hipótese inicial de que repositórios mais populares tendem a ter características de qualidade superiores não foi totalmente confirmada pelos dados analisados. Embora existam correlações estatísticas em algumas métricas, como DIT, a força dessas correlações é insignificante, e a grande dispersão dos dados sugere a influência de múltiplos fatores na popularidade dos repositórios. Portanto, a relação entre a popularidade dos repositórios e suas características de qualidade não é direta nem linear.

-   **RQ 03.** Qual a relação entre a atividade dos repositórios e as suas características de qualidade?
    | | |
    | ---- | ---- |
    | ![Gráfico 9 (CBO × Releases)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/d12e288a-f50e-4de1-b9cd-496e7903672e) | ![Gráfico 10 (DIT × Releases)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/80f8f39d-4b0b-41bd-af2b-7e2978cbcb39) |
    | ![Gráfico 11 (LCOM × Releases)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/fc10facd-cdea-4065-b0d8-d796aedb2cc3) | ![Gráfico 12 (Heatmap Atividade)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/77488551/18dbfb7c-088a-4603-bcbf-d4ed331b61a4) |

**<h4 align="center">Coeficiente de Spearman</h4>**

<div align="center" style="display:flex;">

|         | CBO                       | DIT Máx                  | LCOM                      |
| :------ | :------------------------ | :----------------------- | :------------------------ |
| ρ (rho) | 0.35                      | 0.35                     | 0.3                       |
| p-value | 2.1819 × 10<sup>-27</sup> | 4.237 × 10<sup>-28</sup> | 3.5432 × 10<sup>-20</sup> |

</div>

A análise dos gráficos que relacionam as métricas CK (CBO, DIT, LCOM) com a atividade dos repositórios Java, medida pelo número de releases, revela correlações estatisticamente significativas entre essas métricas e a atividade dos projetos.

No caso do CBO, embora a correlação seja baixa e positiva, a análise indica que repositórios com maior acoplamento tendem a ter mais atividade, refletida em um maior número de releases. Essa relação, no entanto, não é forte e pode ser influenciada por outros fatores, como a natureza do projeto e a frequência de updates.

Similarmente, o DIT apresenta uma correlação baixa e positiva com a atividade dos repositórios. Repositórios com maior profundidade de herança também tendem a ter mais atividade, mas essa relação não é determinística e pode ser influenciada por outros fatores além do DIT.

No caso do LCOM, a correlação é baixa e positiva, indicando que repositórios com maior falta de coesão entre métodos tendem a ter uma atividade ligeiramente maior. No entanto, essa relação é fraca e pode ser influenciada por diversos outros fatores, como a natureza do projeto e a maturidade do processo de desenvolvimento.

Portanto, a hipótese levantada sugere que repositórios com maior atividade, medida pelo número de releases, podem indicar características de qualidade superiores. Uma atividade contínua, com uma comunidade ativa de desenvolvedores, pode resultar em melhorias constantes e um código com características como menor acoplamento, menor profundidade de herança e maior coesão entre métodos. No entanto, é importante considerar que a atividade não é o único indicador de qualidade, e outros fatores também desempenham um papel significativo na determinação da qualidade de um repositório Java.

-   **RQ 04.** Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?
    | | |
    | ---- | ---- |
    | ![Gráfico 13 (CBO × Tamanho)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/8564d149-7932-4fe6-b6c8-f90afde47271) | ![Gráfico 14 (DIT × Tamanho)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/526e4044-5281-4c31-81bb-517fca0d24d7) |
    | ![Gráfico 15 (LCOM × Tamanho)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/90854484/62d9977b-628c-460f-8443-6be27e057dae) | ![Gráfico 6 (Heatmap Tamanho)](https://github.com/NikolasLouret/lab-experimentacao-software-02/assets/77488551/b20639b5-e6cf-47ba-93cf-2f14c78e783a) |

**<h4 align="center">Coeficiente de Spearman</h4>**

<div align="center" style="display:flex;">

|         | CBO                      | DIT Máx                    | LCOM                      |
| :------ | :----------------------- | :------------------------- | :------------------------ |
| ρ (rho) | 0.39                     | 0.79                       | 0.5                       |
| p-value | 1.848 × 10<sup>-34</sup> | 4.0286 × 10<sup>-197</sup> | 6.0394 × 10<sup>-60</sup> |

</div>


A hipótese inicial levantada sugere que repositórios com um maior volume de código, medido pelo LOC, tendem a apresentar características de qualidade inferiores. Essa suposição se baseia na ideia de que um código extenso pode indicar maior complexidade, dificultando a manutenção e aumentando a probabilidade de problemas de qualidade, como acoplamento excessivo. Portanto, espera-se que um código mais enxuto, com menos linhas de código e comentários, apresente uma melhor qualidade em termos de menor acoplamento entre objetos, menor profundidade na árvore de herança e maior coesão entre métodos.

Ao analisar os gráficos que correlacionam métricas como CBO, DIT e LCOM com o tamanho dos repositórios Java (medido pelo LOC), é possível observar diferentes padrões de relação entre tamanho e características de qualidade.

No caso do CBO, há uma correlação baixa e positiva com o tamanho, indicando que à medida que o CBO aumenta, o LOC também tende a aumentar. No entanto, essa relação baixa e pode ser influenciada por outros fatores além do acoplamento entre objetos.

Para o DIT, a correlação é alta e positiva com o tamanho. Isso significa que, conforme a profundidade da árvore de herança aumenta, o LOC também aumenta consideravelmente.

Por fim, o LCOM também apresenta uma correlação moderada e positiva com o tamanho. À medida que a falta de coesão entre métodos aumenta, o LOC tende a aumentar, embora essa relação não seja linear e possa ser influenciada por outros fatores.

## Conclusão

Ao analisar a relação entre a popularidade, maturidade, atividade e tamanho dos repositórios Java com suas características de qualidade, várias conclusões importantes emergem. Primeiramente, não foi encontrada uma ligação direta entre as métricas CK do CBO, DIT e LCOM e a popularidade dos repositórios. Embora algumas correlações estatisticamente significativas tenham sido observadas, como no caso do DIT, a força dessas correlações foi mínima, indicando que múltiplos fatores influenciam a popularidade, como a utilidade do projeto e a qualidade da documentação. Da mesma forma, a maturidade dos repositórios não apresentou uma correlação clara com as métricas de qualidade analisadas, sugerindo a influência de diversos fatores além dessas características.

Quando se trata da atividade dos repositórios, as correlações estatisticamente significativas entre métricas como CBO, DIT e LCOM e o número de releases indicam uma relação, porém fraca e não determinística. Isso sugere que outros elementos, como a natureza do projeto e a participação da comunidade, têm um papel significativo na atividade dos repositórios, além das características de qualidade analisadas. Por fim, em relação ao tamanho dos repositórios, foi observada uma correlação baixa a moderada com as métricas CK, indicando que repositórios maiores podem ter características de qualidade inferiores, embora essa relação não seja direta nem linear.

Essas conclusões destacam a complexidade e a diversidade de fatores que influenciam a qualidade dos repositórios Java. É essencial adotar uma abordagem holística e considerar uma ampla gama de métricas e contextos ao avaliar a qualidade de um repositório de software.
