import streamlit as st

st.title(':rainbow[Saúde mental e produtos estéticos]')
tab1, tab2, tab3, tab4 = st.tabs(["Neurociência", "Cosméticos", "Psicologia", "Créditos"])

with tab1:
    st.header(":red[O que é neurociência?]")
    st.write(
        "A neurociência :red[estuda o sistema nervoso e as suas funcionalidades]. As áreas do corpo que são estudadas são: o "
        "cérebro, sistema periférico e medula espinhal."
        " Esses órgãos fazem parte do sistema nervoso e coordenam o corpo humano. A neurociência também estuda :red[fenômenos da mente humana]."
        " É um ramo da :red[biologia], porém pode colaborar com outras áreas como a educação, medicina, comunicação, química, entre outros campos."
    )

    st.subheader(':red[Neurociência comportamental]')
    st.write('A neurociência comportamental estuda os :red[comportamentos humanos, analisa a conexão entre neurotransmissores e fenômenos psicológicos]. '
             'Ela também investiga :red[transtornos mentais e distúrbios do sistema nervoso]. Quando aplicada nos ambientes de trabalho, essa ciência permite criar rotinas mais saudáveis.')

    st.divider()

    st.header(":blue[Tecnologias da neurociência]")

    st.write(
        "As tecnologias na medicina, especialmente no campo da neurociência, estão se :blue[desenvolvendo rapidamente], revolucionando o :blue[diagnóstico e "
        "tratamento de doenças neurológicas]. Aqui estão exemplos de algumas inovações importantes:"
        )
    st.write(
        ":blue[1. Neuroimagem:] Tecnologias como ressonância magnética funcional (fMRI), tomografia por emissão de pósitrons (PET) e magnetoencefalografia (MEG) "
        "permitem que cientistas e médicos observem a atividade cerebral em tempo real. Essas ferramentas são essenciais para o diagnóstico de "
        "tumores cerebrais, epilepsia e doenças neurodegenerativas como Alzheimer e Parkinson.")

    st.write( ":blue[2. Estimulação Cerebral Profunda (DBS):] Esta técnica envolve a implantação de eletrodos no cérebro para enviar pulsos elétricos para áreas específicas. "
        "DBS é usado principalmente para tratar a doença de Parkinson, tremor essencial e distonia, e pode proporcionar alívio significativo dos sintomas.")

    st.write(":blue[3. Interface Cérebro-Computador (BCI):] A BCI permite a comunicação direta entre o cérebro e dispositivos externos. Isto seria particularmente "
        "útil para pacientes com paralisia ou outros distúrbios de movimento graves, permitindo-lhes controlar membros protéticos, computadores e outros"
        " dispositivos usando apenas os seus pensamentos.")

    st.write(":blue[4. Neuropróteses:] são dispositivos controlados pelo cérebro. Essas próteses podem ser integradas ao sistema nervoso, permitindo aos usuários "
        "controlar o membro protético com alta precisão.")

    st.write(":blue[5. Terapias Genéticas e Terapias Celulares:] Essas abordagens inovadoras estão sendo exploradas para tratar doenças neurológicas hereditárias e"
        " adquiridas. A terapia genética envolve a modificação de genes nas células de um paciente para tratar ou prevenir doenças. A terapia celular usa"
        " células-tronco para substituir ou reparar células danificadas no cérebro.")

    st.write(":blue[6. Inteligência Artificial (IA) e Aprendizado de Máquina (Machine Learning):] A inteligência artificial é usada para analisar grandes quantidades "
        "de dados neurais para ajudar a identificar padrões e prever a progressão de doenças. Isso pode melhorar significativamente o diagnóstico e o "
        "tratamento personalizado para cada paciente.")

    st.write(":blue[7. Realidade Virtual (VR) e Realidade Aumentada (AR):] Essas tecnologias são usadas na neurorreabilitação "
             "para ajudar os pacientes a recuperarem funções motoras e cognitivas após lesão cerebral. Os programas de"
             "VR e AR podem simular ambientes e tarefas para praticar habilidades motoras e cognitivas em um ambiente ""controlado.")


with tab2:
    st.header(":violet[Cosméticos e suas propriedades]")

    st.write("É inegável que os cosméticos são uma :violet[ferramenta de apoio emocional] e ajudam bastante na :violet[auto estima] de quem"
             " está utilizando o produto tanto por conseguir melhorar a aparência externa e criar um :violet[sentimento de "
             "pertencimento].")
    st.write("A arte da cosmetologia é muito antiga e abrange muitas áreas e produtos como perfumes hidratantes óleos e maquiagens diversas."
             "Essa prática surgiu na :violet[antiguidade egípcia], e tinha como propósito inicial encobrir o cheiro de cadáveres, perfumar o ambiente e fins medicinais.")


    st.write("A cosmetologia tambem pode ajudar na :violet[saúde fisica] do individuo, como por exemplo :violet[diminuir a oleosidade da pele e cabelo além de prevenir doenças]. "
             "Os principais compostos da maioria dos cosméticos são plantas principalmente :violet[flores], que possuem princípios ativos desejados para o produto "
             "seja um :violet[aroma, cor ou efeitos medicinais].")

    st.write("Algumas das flores mais utilizadas para este propósito são:")

    st.write("- :violet[Rosa]")

    st.write("- :violet[Lavanda]")

    st.write("- :violet[Jasmin]")

    st.write("- :violet[Alecrim]")

    st.write("- :violet[Hortelã]")

    st.write("- :violet[Cerejeira]")

    st.write("- :violet[Lírio]")


with tab3:
    st.header(":rainbow[Psicologia das cores]")

    st.write(" É um estudo sobre a capacidade que o nosso cérebro tem de :rainbow[identificar uma cor e transform á -la numa sensação ou sentimento].")

    st.write("Quando falamos em persuasão, falamos em emoção. E as cores têm a capacidade de :rainbow[definir o nosso humor, as nossas emoções e "
             "até mesmo os nossos desejos]. Na área do marketing e da publicidade onde todos os detalhes são pensados ao máximo, de forma a"
             " causar o impacto pretendido no consumidor, as cores não são exceção. :rainbow[Todas as cores são pensadase testadas de acordo com a "
             "emoção que cada marca pretende despertar nos seus consumidores].")

    st.divider()

    st.header("Cores e como te afetam")

    st.subheader(":red[Vermelho]")

    st.write("Essa cor primária está ligada ao :red[dinamismo], ou seja, a vontade de se movimentar e agir. Experiências mostram que o vermelho consegue :red[estimular o"
             " corpo humano], fazendo com que ocorra um :red[aumento na pressão sanguínea e do número de batimentos cardíacos], por exemplo.")

    st.write("- Raiva")

    st.write("- Paixão")

    st.write("- Ira")

    st.write("- Calor")

    st.write("- Perigo")

    st.write("- Violência")

    st.write("- Fúria")

    st.write("- Excitação")

    st.subheader(":orange[Amarelo]")

    st.write(
        "Por ser uma cor quente, o amarelo também transmite a sensação de :orange[dinamismo e estímulo]. É considerada a cor do :orange[otimismo "
        "e da energia], segundo a psicologia das cores. Tem ainda a capacidade de estimular a :orange[concentração e o intelecto] das pessoas.")

    st.write(
        "Outra sensação associada a esta cor é o de :orange[conforto  e felicidade]. Entre alguns dos sentimentos que o amarelo "
        "também está relacionado, destaque para:")

    st.write("- Sabedoria")

    st.write("- Alegria")

    st.write("- Otimismo")

    st.write("- Inveja")

    st.write("- Doença")

    st.write("- Idealismo")

    st.write("- Covardia")

    st.subheader(":orange[Laranja]")

    st.write(
        "O laranja é uma cor secundária que, assim como o vermelho, também transmite a ideia de :orange[movimento, excitação e desejo "
        "de ação]. Mas, diferente do primeiro, o laranja não chega a ser tão impactante.")

    st.write(
        "A psicologia das cores atribui a sensação de :orange[alegria, sociabilidade e animação] para o laranja. Entre outros "
        "sentimentos relacionados a esta cor, destaque para:")

    st.write("- Humor")

    st.write("- Energia")

    st.write("- Calor")

    st.write("- Extravagância")

    st.write("- Entusiasmo")

    st.write("- Amigabilidade")

    st.subheader(":violet[Roxo]")

    st.write(
    "Essa cor atua diretamente na área cerebral destinada à :violet[criatividade], ou seja, :violet[promove um estímulo para a solução de "
    "bloqueios criativos]. Além disso, a sensação de :violet[calmaria e tranquilidade] também estão relacionados com o roxo. Por essa "
    "razão, vários temas espirituais e ligados à fé são representados com esta cor.")

    st.write(
    "O roxo ainda representa a imagem do :violet[sucesso, da nobreza e da riqueza]. Entre outras relações, destaque para:")

    st.write("- Erotismo")

    st.write("- Mistério")

    st.write("- Sabedoria")

    st.write("- Arrogância")

    st.write("- Sensibilidade")

    st.write("- Intimidade")

    st.subheader(":blue[Azul]")

    st.write(
    "O azul transmite a ideia de :blue[calma, serenidade e tranquilidade]. Por esse motivo, costuma ser comum o seu uso para "
    "representar :blue[profissionalismo, estabilidade e segurança].")

    st.write(
    "Alguns dos sentimentos relacionados com o azul, segundo a psicologia das cores, são:")

    st.write("- Lealdade")

    st.write("- Tranquilidade")

    st.write("- Harmonia")

    st.write("- Confiança")

    st.write("- Limpeza")

    st.write("- Frio")

    st.write("- Depressão")

    st.subheader(":green[Verde]")

    st.write(
        "Para a psicologia das cores, o verde está associado com a :green[saúde, a vitalidade, a natureza e fertilidade]. Para os "
        "psicólogos, essa cor possui a capacidade de :green[acalmar as pessoas e aliviar o stress].")

    st.write(
        "Entre os outros sentimentos que esta cor desperta, destaque para:")

    st.write("- Perseverança")

    st.write("- Orgulho")

    st.write("- Boa sorte")

    st.write("- Juventude")

    st.write("- Generosidade")

    st.write("- Imaturidade")

    st.write("- Ciúme")

with tab4:
    st.header(':green[Créditos]')

    st.subheader(":red[Neurociência] - Julia Catroli")

    st.subheader(":blue[Tecnologias da Medicina] - Manuela Selhorst")

    st.subheader(":violet[Cosméticos] - João Guilherme")

    st.subheader(":rainbow[Bem estar físico e mental (Psicologia)] - Raissa Costa")

    st.subheader(":green[Programação] - Alice Santesso")

    st.header("MUITO OBRIGADO!")
