BEGIN TRY:
    INSERT INTO test_eth2.transactions FROM INFILE '/Users/foooox/eth_data/eth_data/output/transactions/start_block=00390000/end_block=00399999/transactions_00390000_00399999.csv' FORMAT CSVWithNames;
END TRY
BEGIN CATCH
SELECT ERROR_MESSAGE()
END CATCH;