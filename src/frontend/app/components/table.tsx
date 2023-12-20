import React, { useState } from 'react';
import styles from '../styles/Table.module.css';

const Table = ({ data }) => {
    const [selectedRow, setSelectedRow] = useState<number | null>(null);

    return (
        <table className={styles.tabela}>
            <thead>
                <tr>
                    <th>Id SAS</th>
                    <th>Nome usuário</th>
                    <th>Nome Produto</th>
                    <th>Quantidade</th>
                    <th>Data</th>
                </tr>
            </thead>
            <tbody>
                {data.map((item, index) => (
                    <tr
                        key={index}
                        className={selectedRow === index ? styles.selectedRow : ""}
                        onClick={() => setSelectedRow(index)}
                    >
                        <td>{item.Id_P}</td>
                        <td>{item.Name}</td>
                        <td>{item.Name_P}</td>
                        <td>{item.amount}</td>
                        <td>{item.data}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default Table;
