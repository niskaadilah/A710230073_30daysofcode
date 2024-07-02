import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog

class TicketApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle('Ticket App')
        self.setGeometry(100, 100, 600, 400)

        # Set up the layout
        layout = QVBoxLayout()

        # Create a table to display tickets
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Ticket ID', 'Event', 'Price'])

        # Create a button to add tickets and connect it to a function
        self.add_ticket_button = QPushButton('Add Ticket')
        self.add_ticket_button.clicked.connect(self.add_ticket)

        # Add the table and button to the layout
        layout.addWidget(self.table)
        layout.addWidget(self.add_ticket_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def add_ticket(self):
        # Get ticket information from user input
        ticket_id, ok1 = QInputDialog.getText(self, 'Input Ticket ID', 'Enter Ticket ID:')
        event, ok2 = QInputDialog.getText(self, 'Input Event', 'Enter Event Name:')
        price, ok3 = QInputDialog.getText(self, 'Input Price', 'Enter Ticket Price:')

        if ok1 and ok2 and ok3:
            # Get the current row count and insert a new row
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)

            # Add the ticket information to the table
            self.table.setItem(row_count, 0, QTableWidgetItem(ticket_id))
            self.table.setItem(row_count, 1, QTableWidgetItem(event))
            self.table.setItem(row_count, 2, QTableWidgetItem(price))

def main():
    app = QApplication(sys.argv)
    window = TicketApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
