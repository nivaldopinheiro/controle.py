from PyQt6 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_doacao"
)


def editar_dados():
    global numero_id

    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tabela")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM tabela WHERE id=" + str(valor_id))
    doacao = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(doacao[0][0]))
    tela_editar.lineEdit_2.setText(str(doacao[0][1]))
    tela_editar.lineEdit_3.setText(str(doacao[0][2]))
    tela_editar.lineEdit_4.setText(str(doacao[0][3]))
    tela_editar.lineEdit_5.setText(str(doacao[0][4]))
    tela_editar.lineEdit_6.setText(str(doacao[0][5]))
    tela_editar.lineEdit_7.setText(str(doacao[0][6]))
    tela_editar.lineEdit_8.setText(str(doacao[0][7]))
    numero_id = valor_id


def salvar_valor_editado():
    global numero_id

    # ler dados do lineEdit
    doacao = tela_editar.lineEdit.text()
    parceiro = tela_editar.lineEdit_2.text()
    cpf_cnpj = tela_editar.lineEdit_3.text()
    descricao = tela_editar.lineEdit_4.text()
    data_doacao = tela_editar.lineEdit_5.text()
    quantidade_kg = tela_editar.lineEdit_6.text()
    categoria = tela_editar.lineEdit_7.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute(
        "UPDATE tabela SET doacao = '{}', parceiro = '{}', cpf_cnpj = '{}', descrição ='{}', data_doacao ='{}', quantidade_kg ='{}', categoria ='{}' WHERE id = {}".format(
            doacao, parceiro, cpf_cnpj, descricao, data_doacao, quantidade_kg, categoria, numero_id))
    banco.commit()

    # atualizar as janelas
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()


def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tabela")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM tabela WHERE id =" + str(valor_id))


def gerar_pdf():
    cursor = banco.cursor()
    comando_mysql = "SELECT * FROM tabela"
    cursor.execute(comando_mysql)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_doacao.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "DOAÇÃO")
    pdf.drawString(210, 750, "PARCEIRO")
    pdf.drawString(310, 750, "CPF/CNPJ")
    pdf.drawString(410, 750, "DESCRIÇÃO")
    pdf.drawString(510, 750, "DATA_DOAÇÃO")
    pdf.drawString(610, 750, "QUANTIDADE_KG")
    pdf.drawString(710, 750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][4]))
        pdf.drawString(510, 750 - y, str(dados_lidos[i][5]))
        pdf.drawString(610, 750 - y, str(dados_lidos[i][6]))
        pdf.drawString(710, 750 - y, str(dados_lidos[i][7]))
    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()

    if formulario.radioButton.isChecked():
        print("Categoria Gato selecionada")
        categoria = "Gato"

    elif formulario.radioButton_2.isChecked():
        print("Categoria Cachorro selecionada")

        categoria = "Cachorro"
    else:
        print("Categoria Outros selecionada")
        categoria = "Outros"

    print("Doacao:", linha1)
    print("Parceiro:", linha2)
    print("Cpf/Cnpj", linha3)
    print("Descrição", linha4)
    print("data_doação", linha5)
    print("Quantidade Kg", linha6)

    cursor = banco.cursor()
    comando_mysql = "INSERT INTO tabela (doacao, parceiro, cpf_ cnpj, descricao, data_doacao, quantidade_kg, categoria) VALUES (%s,%s,%s,%s,%,%,%)"
    dados = (str(linha1), str(linha2), str(linha3),str(linha4),str(linha5),str(linha6),str(linha6), categoria)
    cursor.execute(comando_mysql, dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")

def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tabela"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(7)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 7):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
tela_editar = uic.loadUi("menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)
segunda_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_valor_editado)

formulario.show()
app.exec()
