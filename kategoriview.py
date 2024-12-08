from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector as mc


class Ui_Kategori(object):
    def setupUi(self, Kategori):
        Kategori.setObjectName("Kategori")
        Kategori.resize(500, 500)

        # Layout untuk Input ID dan Nama Kategori
        self.inputLayout = QtWidgets.QWidget(Kategori)
        self.inputLayout.setGeometry(QtCore.QRect(10, 10, 480, 80))
        self.inputLayout.setObjectName("inputLayout")

        self.formLayout = QtWidgets.QFormLayout(self.inputLayout)
        self.formLayout.setObjectName("formLayout")

        self.labelId = QtWidgets.QLabel(self.inputLayout)
        self.labelId.setFont(QtGui.QFont("Arial", 12))
        self.labelId.setText("ID Kategori:")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelId)

        self.lineEditId = QtWidgets.QLineEdit(self.inputLayout)
        self.lineEditId.setFont(QtGui.QFont("Arial", 12))
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditId)

        self.labelName = QtWidgets.QLabel(self.inputLayout)
        self.labelName.setFont(QtGui.QFont("Arial", 12))
        self.labelName.setText("Nama Kategori:")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)

        self.lineEditName = QtWidgets.QLineEdit(self.inputLayout)
        self.lineEditName.setFont(QtGui.QFont("Arial", 12))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditName)

        # Tombol Insert dan Load
        self.buttonLayout = QtWidgets.QWidget(Kategori)
        self.buttonLayout.setGeometry(QtCore.QRect(10, 100, 480, 50))
        self.buttonLayout.setObjectName("buttonLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonLayout)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButtonInsert = QtWidgets.QPushButton(self.buttonLayout)
        self.pushButtonInsert.setFont(QtGui.QFont("Arial", 12))
        self.pushButtonInsert.setText("INSERT DATA")
        self.horizontalLayout.addWidget(self.pushButtonInsert)

        self.pushButtonLoad = QtWidgets.QPushButton(self.buttonLayout)
        self.pushButtonLoad.setFont(QtGui.QFont("Arial", 12))
        self.pushButtonLoad.setText("LOAD DATA")
        self.horizontalLayout.addWidget(self.pushButtonLoad)

        # Label untuk Menampilkan Hasil Operasi
        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(10, 160, 480, 20))
        self.labelResult.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        # Tabel untuk Menampilkan Data
        self.tableWidget = QtWidgets.QTableWidget(Kategori)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 480, 250))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID Kategori", "Nama Kategori"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Fungsi Tombol
        self.pushButtonInsert.clicked.connect(self.insertkategori)
        self.pushButtonLoad.clicked.connect(self.loadkategori)

        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def insertkategori(self):
        idkat = self.lineEditId.text()
        namakat = self.lineEditName.text()

        if not idkat or not namakat:
            self.labelResult.setText("ID dan Nama Kategori tidak boleh kosong.")
            return

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan",
            )
            cursor = mydb.cursor()
            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            val = (idkat, namakat)
            cursor.execute(sql, val)
            mydb.commit()

            self.labelResult.setText("Data Kategori Berhasil Disimpan")
            self.lineEditId.clear()
            self.lineEditName.clear()
        except mc.Error as e:
            self.labelResult.setText(f"Data Kategori Gagal Disimpan: {e}")

    def loadkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan",
            )
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM kategori ORDER BY id ASC")
            result = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.labelResult.setText("Data Kategori Berhasil Ditampilkan")
        except mc.Error as e:
            self.labelResult.setText(f"Data Kategori Gagal Diload: {e}")

    def retranslateUi(self, Kategori):
        Kategori.setWindowTitle("Form Kategori")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())
