import APP_datasets
import main_script

main_script.policies_order() #Choose the policies order
main_script.sort_with_tiebreaker(APP_datasets.AVIONS_INITIAL, main_script.policies_orders) #Test for 24 Planes
main_script.sort_with_tiebreaker(APP_datasets.avions_diplomatic_50, main_script.policies_orders) #Test for 50 Planes
main_script.sort_with_tiebreaker(APP_datasets.avions_chaos_100 , main_script.policies_orders) #Test for 100 Planes
