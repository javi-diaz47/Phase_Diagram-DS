from DynamicSystem import DynamicSystem


def main():

    print('bitch')    
    ds = DynamicSystem()

    print(f'{ds.A}')

    ds.get_cp()

    ds.cp.show_props()

    ds.display_system()

if __name__ == "__main__":
    main()