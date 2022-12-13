echo "per_hour_snapp,per_hour_tapsi,per_km_snapp,per_km_tapsi,total_snapp_income,total_tapsi_income,total_hour,total_km" >> summary
for file in *.csv; do
    python3 summary.py $file;
done
mv summary summary.csv