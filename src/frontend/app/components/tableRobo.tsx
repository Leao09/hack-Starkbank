import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../styles/Table.module.css';

interface Dados {
  id: number;
  X: string;
  Y: string;
}

const Table: React.FC = () => {
  const [tableData, setTableData] = useState<Dados[]>([]); // Corrigido aqui
  const [selectedRow, setSelectedRow] = useState<number | null>(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/robo')
      .then(response => setTableData(response.data as Dados[])) // Corrigido aqui
      .catch(error => console.error('Erro ao obter dados da tabela:', error));
  }, []);

  return (
    <table className={styles.tabela}>
      <thead>
        <tr>
          <th>Id</th>
          <th>X</th>
          <th>Y</th>
        </tr>
      </thead>
      <tbody>
        {tableData.map((item, index) => (
          <tr
            key={index}
            className={selectedRow === index ? styles.selectedRow : ""}
            onClick={() => setSelectedRow(index)}
          >
            <td>{item.id}</td>
            <td>{item.X}</td>
            <td>{item.Y}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
