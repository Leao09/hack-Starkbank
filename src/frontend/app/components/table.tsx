import React, { useState } from 'react';
import styles from '../styles/Table.module.css'; 

const Table = () => {
const [selectedRow, setSelectedRow] = useState<number | null>(null);
  const data = [
    { nome: "Item 1", id: "ID1", status: "Disponível", quantidade: 10 },
    { nome: "Item 2", id: "ID2", status: "Disponível", quantidade: 20 },
    { nome: "Item 3", id: "ID3", status: "Disponível", quantidade: 30 },
    { nome: "Item 4", id: "ID4", status: "Disponível", quantidade: 40 },
    { nome: "Item 5", id: "ID5", status: "Disponível", quantidade: 50 },
  ];

  return (
    <table className={styles.tabela}>
      <thead>
        <tr>
          <th>Nome</th>
          <th>ID</th>
          <th>Status estoque</th>
          <th>Quantidade</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr
            key={index}
            className={selectedRow === index ? styles.selectedRow : ""}
            onClick={() => setSelectedRow(index)}
          >
            <td>{item.nome}</td>
            <td>{item.id}</td>
            <td>{item.status}</td>
            <td>{item.quantidade}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
