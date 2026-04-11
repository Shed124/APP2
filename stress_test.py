import APP_datasets
import main_script

main_script.policies_order()
main_script.sort_with_tiebreaker(APP_datasets.AVIONS_INITIAL, policies_orders) #Test for 23 Planes
main_script.sort_with_tiebreaker(APP_datasets.avions_diplomatic_50, policies_orders) #Test for 50 Planes
main_script.sort_with_tiebreaker(APP_datasets.avions_chaos_100 , policies_orders) #Test for 100 Planes
